from django.contrib import admin
import data_wizard

from .models import Inventario

admin.site.register(Inventario)
data_wizard.register(Inventario)