from django.urls import path
from rest_direccion import views
from rest_direccion.views import datos_direccion,detalle_direccion
from rest_direccion.viewslogin import login

urlpatterns = [
    path('datos_direccion/', datos_direccion, name = "datos_direccion"),
    path('detalle_direccion/<id>',detalle_direccion, name="detalle_direccion"),
    path('login', login, name = "login"),
]