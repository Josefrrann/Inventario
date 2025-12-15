from django.shortcuts import render, redirect
from django.contrib import messages
from Inventario.models import Inventario

def guardar_inventario(request):
    if request.method == 'POST':
        # Iteramos sobre todos los datos enviados
        for key, value in request.POST.items():
            # Buscamos los campos que empiecen con "cantidad_"
            if key.startswith('cantidad_'):
                try:
                    # Extraemos el ID del producto del nombre del input (ej: cantidad_5 -> 5)
                    producto_id = key.split('_')[1]
                    nuevo_valor = int(value)
                    
                    # Actualizamos el producto
                    # Usamos update() directo para ser más eficientes
                    Inventario.objects.filter(id=producto_id).update(existencias=nuevo_valor)
                    
                except (ValueError, IndexError):
                    continue
        
        messages.success(request, "Inventario actualizado correctamente.")
        return redirect('lista_inventario') # Redirige a tu vista principal

    return redirect('lista_inventario')
