from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from .views import index
from . import views
from menu.views import recuperacion, recuperacion2, recuperacion3,entorno,carrito,form,agregar_platillos, platillos,eliminar_platillos, modificar_platillos, perfil,editar_perfil, pas_nuevo_usuario,val_nuevo_usuario,nosotros, crearnombre, registro, crear_usuario, cambiar_contra, cambiar_contra, val_cambiar_contra, verificarcorreo, cerrar_sesion, iniciar_sesion, modificar_form, editarperfil
# define las url y las asocia a las views
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('eliminar_platillos/', views.eliminar_platillos, name='eliminar_platillos'),
    path('cambiar-imagen/', views.cambiar_imagen, name='cambiar_imagen'),
    path('register/val_nuevo_usuario.html', views.val_nuevo_usuario, name='val_nuevo_usuario'),
    path('register/pas_nuevo_usuario.html', views.pas_nuevo_usuario, name='pas_nuevo_usuario'),
    path('mi_formulario/', views.mi_formulario, name='mi_formulario'),
    path('cambiarcontra/', views.cambiarcontra, name='cambiarcontra'),
    path('cambiarcontra2/', views.cambiarcontra2, name='cambiarcontra2'),
    path('cerrar_sesion/', views.cerrar_sesion, name="cerrar_sesion"),
    path('iniciar_sesion/', views.iniciar_sesion, name="iniciar_sesion"),
    path('recuperacion.html', views.recuperacion, name="recuperacion"),
    path('recuperacion2.html', views.recuperacion2, name="recuperacion2"),
    path('recuperacion3.html', views.recuperacion3, name="recuperacion3"),
    path('entorno.html', views.entorno, name="entorno"),
    path('carrito.html', views.carrito, name="carrito"),
    path('form.html', views.form, name="form"),
    path('agregar_platillos.html', views.agregar_platillos, name="agregar_platillos"),
    path('platillos.html', views.platillos, name="platillos"),
    path('eliminar_platillos.html', views.eliminar_platillos, name="eliminar_platillos"),
    path('Perfil.html', views.perfil, name="perfil"),
    path('editar_perfil.html', views.editar_perfil, name="editar_perfil"),
    path('editarperfil/', views.editarperfil, name="editarperfil"),
    path('pas_nuevo_usuario.html', views.pas_nuevo_usuario, name="pas_nuevo_usuario"),
    path('val_nuevo_usuario.html', views.val_nuevo_usuario, name="val_nuevo_usuario"),
    path('nosotros.html', views.nosotros, name="nosotros"),
    path('registro.html', views.registro, name="registro"),
    path('crear_usuario/', views.crear_usuario, name="crear_usuario"),
    path('cambiar_contra.html', views.cambiar_contra, name="cambiar_contra"),
    path('val_cambiar_contra.html', views.val_cambiar_contra, name="val_cambiar_contra"),
    path('verificarcorreo.html', views.verificarcorreo, name="verificarcorreo"),
    path('modificar_platillos.html', views.modificar_platillos, name="modificar_platillos"),
    path('modificar_form.html', views.modificar_form, name="modificar_form"),
]
