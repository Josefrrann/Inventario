from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_inventario, name='lista_inventario'),
    path('anadir/', views.anadir_producto, name='anadir_producto'),
    path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('ajustar/<int:pk>/', views.ajustar_existencias, name='ajustar_existencias'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
]