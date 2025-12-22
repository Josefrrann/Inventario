from django.shortcuts import render, redirect, get_object_or_404
from .models import Inventario
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F, Q 
from django.contrib.auth.models import User
from .forms import ProductoForm

@login_required
def lista_inventario(request):
    
    query = request.GET.get('q')
    stock_filter = request.GET.get('stock_filter')

    inventarios = Inventario.objects.order_by('descripcion')

    if query:
        inventarios = inventarios.filter(
            Q(codigo_producto__icontains=query) | Q(descripcion__icontains=query)
        )

    if stock_filter == 'low':
        inventarios = inventarios.filter(existencias=1)
    elif stock_filter == 'none':
        inventarios = inventarios.filter(existencias=0)

    return render(request, 'Inventarios.html', {'inventarios': inventarios})


@login_required
def anadir_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f"Producto '{producto.descripcion}' añadido exitosamente.")
            return redirect('lista_inventario')
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form, 'titulo': 'Añadir Producto'})

@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Inventario, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto_actualizado = form.save()
            messages.success(request, f"Producto '{producto_actualizado.descripcion}' actualizado exitosamente.")
            return redirect('lista_inventario')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_form.html', {'form': form, 'titulo': 'Editar Producto'})

@login_required
def ajustar_existencias(request, pk):
    producto = get_object_or_404(Inventario, pk=pk)
    if request.method == 'POST':
        try:
            cantidad = int(request.POST.get('cantidad', 0))
            action = request.POST.get('action')

            if action == 'descontar':
                if producto.existencias >= cantidad:
                    producto.existencias -= cantidad
                    producto.save()
                    messages.success(request, f"Se descontaron {cantidad} unidades de '{producto.descripcion}'.")
                else:
                    messages.error(request, f"No se puede descontar. Stock insuficiente para '{producto.descripcion}'.")
            
            elif action == 'incrementar':
                producto.existencias += cantidad
                producto.save()
                messages.success(request, f"Se añadieron {cantidad} unidades a '{producto.descripcion}'.")

        except (ValueError, TypeError):
            messages.error(request, "La cantidad debe ser un número válido.")
            
    return redirect('lista_inventario')

@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Inventario, pk=pk)
    if request.method == 'POST':
        descripcion_producto = producto.descripcion
        producto.delete()
        messages.success(request, f"Producto '{descripcion_producto}' eliminado exitosamente.")
    return redirect('lista_inventario')

@login_required
def lista_usuarios(request):
    if not request.user.is_superuser:
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('lista_inventario')
    usuarios = User.objects.all().order_by('username')
    return render(request, 'usuarios.html', {'usuarios': usuarios})
