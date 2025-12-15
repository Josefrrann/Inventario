from django.urls import path
from . import views

urlpatterns = [
    # ... tus otras urls ...
    path('guardar-inventario/', views.guardar_inventario, name='guardar_inventario'),
]
