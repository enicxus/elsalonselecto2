from django.contrib import admin
from .models import Pedido, Detalle, Comida, Usuario, Pregunta, Rol, Direccion, Comuna, Region

# Register your models here.

admin.site.register(Pedido)
admin.site.register(Detalle)
admin.site.register(Comida)
admin.site.register(Usuario)
admin.site.register(Pregunta)
admin.site.register(Rol)
admin.site.register(Direccion)
admin.site.register(Comuna)
admin.site.register(Region)