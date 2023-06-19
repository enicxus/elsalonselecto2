from django.db import models

class Comida(models.Model):
    id_comida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    foto = models.ImageField(upload_to='comida')
    precio = models.IntegerField(default=0)
    especial = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='Usuario')
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=12)
    contrasena = models.CharField(max_length=100)

    def __str__(self) :
        return self.correo

class Tarjeta(models.Model):
    id_tarjeta = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=20)
    titular = models.CharField(max_length=50)
    numero_tarjeta = models.IntegerField()
    codigo_seguridad = models.IntegerField()
    fecha_vencimiento = models.DateField()