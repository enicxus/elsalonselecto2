from django.db import models

class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self) :
        return self.nombre


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

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.nombre

class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    codigo_postal = models.CharField(max_length=20)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.calle

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    clave = models.CharField(max_length=100)
    respuesta = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self) :
        return self.correo


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    fecha_pedido = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=50)
    carrito = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.total

class Detalle(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    comida = models.ForeignKey(Comida, on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.cantidad