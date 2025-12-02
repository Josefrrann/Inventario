# excel/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluye las URLs de tu app 'Inventario'
    path('', include('Inventario.urls')), 
    
    # Añade esta línea para las URLs de autenticación
    path('accounts/', include('django.contrib.auth.urls')),
]
