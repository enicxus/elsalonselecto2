from django.contrib import admin
from .models import   Comida, Usuario, Tarjeta

# Register your models here.

admin.site.register(Tarjeta)
admin.site.register(Comida)
admin.site.register(Usuario)
