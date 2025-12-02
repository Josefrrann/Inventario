from django import forms
from .models import Inventario

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['codigo_producto', 'descripcion', 'existencias', 'precio']
        widgets = {
            'codigo_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'existencias': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }