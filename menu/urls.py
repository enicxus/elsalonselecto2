from django.contrib import admin
from django.urls import path,include
from .views import index 
from . import views
from menu.views import recuperacion, recuperacion2, recuperacion3,entorno,carrito,form,agregar_platillos, platillos,eliminar_platillos,perfil,editar_perfil, pas_nuevo_usuario,val_nuevo_usuario,nosotros, crearnombre, registro, crear_usuario
# define las url y las asocia a las views
urlpatterns = [
    path('', index, name="index"),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('eliminar_platillos/', views.eliminar_platillos, name='eliminar_platillos'),
    path('register/val_nuevo_usuario.html', views.val_nuevo_usuario, name='val_nuevo_usuario'),
    path('register/pas_nuevo_usuario.html', views.pas_nuevo_usuario, name='pas_nuevo_usuario'),
    path('mi_formulario/', views.mi_formulario, name='mi_formulario'),
    path('recuperacion.html', recuperacion, name="recuperacion"),
    path('recuperacion2.html', recuperacion2, name="recuperacion2"),
    path('recuperacion3.html', recuperacion3, name="recuperacion3"),
    path('entorno.html', entorno, name="entorno"),
    path('carrito.html', carrito, name="carrito"),
    path('form.html', form, name="form"),
    path('agregar_platillos.html', agregar_platillos, name="agregar_platillos"),
    path('platillos.html', platillos, name=" platillos"),
    path('eliminar_platillos.html', eliminar_platillos, name="eliminar_platillos"),
    path('Perfil.html', perfil, name="perfil"),
    path('editar_perfil.html', editar_perfil, name="editar_perfil"),
    path('pas_nuevo_usuario.html', pas_nuevo_usuario, name="pas_nuevo_usuario"),
    path('val_nuevo_usuario.html', val_nuevo_usuario, name="val_nuevo_usuario"),
    path('nosotros.html', nosotros, name="nosotros"),
    path('registro.html', registro, name="registro"),
    path('crear_usuario/', crear_usuario, name="crear_usuario"),
]