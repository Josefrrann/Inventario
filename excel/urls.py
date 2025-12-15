# excel/urls.py

from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluye las URLs de tu app 'Inventario'
    path('', include('Inventario.urls')), 
    
    # Añade esta línea para las URLs de autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('guardar-inventario/', core_views.guardar_inventario, name='guardar_inventario'),
]
