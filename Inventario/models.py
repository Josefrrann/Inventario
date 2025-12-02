from django.db import models

class Inventario(models.Model): 
    codigo_producto = models.CharField('CÓDIGO PRODUCTO', max_length=30)
    descripcion = models.CharField('DESCRIPCIÓN', max_length=100)
    existencias = models.PositiveSmallIntegerField('EXISTENCIAS') 
    precio = models.DecimalField('PRECIO', max_digits=10, decimal_places=2) 
