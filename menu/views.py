import random
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Usuario,Comida, Tarjeta
from django.core.mail import send_mail
from django.conf import settings
from random import randint
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

#crea las vistas cada url

def index(request):
    return render(request,'menu/index.html')

def login(request):
    if request.method == 'POST':
        # Procesa los datos del formulario de inicio de sesión
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Busca al usuario por su correo electrónico
            usuario = Usuario.objects.get(correo=email)
            
            # Valida la contraseña cifrada
            if check_password(password, usuario.contrasena):
                # Guarda los datos del usuario en las variables de sesión
                request.session['user_nombre'] = usuario.nombre
                request.session['user_foto'] = usuario.foto.url if usuario.foto else None
                request.session['user_correo'] = usuario.correo
                request.session['user_direccion'] = usuario.direccion
                request.session['user_telefono'] = usuario.telefono
                request.session['user_id'] = usuario.id_usuario
                
                return redirect('entorno')  # Redirige a la página de entorno.html después del inicio de sesión exitoso
            
        except Usuario.DoesNotExist:
            pass
        
    # Si no se encuentra un usuario o la contraseña no es válida, no realiza ninguna acción
    # o si la solicitud no es de tipo POST
    error_message = request.COOKIES.get('error_message')
    response = render(request, 'menu/index.html', {'error_message': error_message})
    response.delete_cookie('error_message')
    return response

def register(request):
    if request.method == 'POST':
        if request.POST.get('action') == 'send_code':
            email = request.POST.get('email')
            codigo = f'{randint(1000, 9999)}-{randint(1000, 9999)}'
            mensaje = f'Tu código de validación es: {codigo}'
            send_mail(
                'Código de validación',
                mensaje,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            request.session['codigo_correo'] = codigo
            request.session['email'] = email
            request.session['nombre'] = request.POST.get('apodo')
            request.session['direccion'] = request.POST.get('direccion')
            request.session['telefono'] = request.POST.get('telefono')
            request.session['contrasena'] = request.POST.get('password')
            
            return redirect('val_nuevo_usuario')

    return render(request, 'registro.html')

def cambiarcontra(request):
    if request.method == 'POST':
        if request.POST.get('action') == 'send_code':
            emailuser = request.session['user_correo']
            codigocontra = f'{randint(1000, 9999)}-{randint(1000, 9999)}'
            mensaje = f'Tu código para cambiar contraseña es: {codigocontra}'
            send_mail(
                'Código de validación',
                mensaje,
                settings.DEFAULT_FROM_EMAIL,
                [emailuser],
                fail_silently=False,
            )

            request.session['codigo_correo_contra'] = codigocontra
            request.session['nuevacontra'] = request.POST.get('nuevapassword')
            request.session['nuevacontraconf'] = request.POST.get('confirmarnuevapassword')

            return redirect('val_cambiar_contra')

    return render(request, 'menu/cambiar_contra.html')

def cambiarcontra2(request):
    if request.method == 'POST':
        codigocontra = request.POST.get('codigo')
        if codigocontra == request.session.get('codigo_correo_contra'):
            nuevacontrasena = request.session.get('nuevacontra')
            confirnuevacontrasena = request.session.get('nuevacontraconf')
            usuario_id = request.session.get('user_id')
            usuario = Usuario.objects.get(id_usuario = usuario_id)
            
            if nuevacontrasena == confirnuevacontrasena:
                
                usuario.contrasena = nuevacontrasena
                usuario.save()

                request.session.pop('contrasena', None)
                
                messages.success(request, 'Contraseña ha sido actualizada correctamente.')
            
            else:
                messages.error(request, 'Las contraseñas no coinciden.')
                
            return redirect('index')
                
        else:
            messages.error(request, 'El código ingresado no es correcto.')
        
        return redirect('val_cambiar_contra')

    return render(request, 'menu/index.html')

"""

def register(request):
    if request.method == 'POST':
        # Procesa los datos del formulario de registro
        #usuario=usuari
        email = request.POST.get('email')
        
        
    return render(request, 'index.html')
"""




def cambiar_imagen(request):
    if request.method == 'POST':
        nuevo_foto = request.POST.get('foto')
        usuario_id = request.session.get('user_id')
        usuario = Usuario.objects.get(id_usuario=usuario_id)
        usuario.foto = nuevo_foto
        usuario.save()
        return redirect('perfil')
    else:
        return render(request, 'menu/cambiar_imagen.html')
    


def verificarcorreo(request):
    return render(request, 'menu/val_cambiar_contra.html')

def val_cambiar_contra(request):
    return render(request, 'menu/val_cambiar_contra.html')

def registro(request):
    return render(request,'menu/registro.html')

def recuperacion(request):
    if request.method == 'POST':
        correo = request.POST['email']
        usuario = Usuario.objects.filter(correo=correo).first()
        if usuario:
            codigo_verificacion = generar_codigo_verificacion()
            # Envío de correo electrónico con el código de verificación
            enviar_correo_recuperacion(correo, codigo_verificacion)
            # Almacenar el código de verificación en la sesión del usuario
            request.session['codigo_verificacion'] = codigo_verificacion
            request.session['correo'] = correo
            return redirect('recuperacion2')
        else:
            messages.error(request, 'No se encontró ningún usuario con ese correo.')
            return redirect('recupcontra')
    return render(request, 'menu/recuperacion.html')


def recuperacion2(request):
    if request.method == 'POST':
        codigo_verificacion = request.POST['codigo_veri']
        if 'codigo_verificacion' in request.session and request.session['codigo_verificacion'] == codigo_verificacion:
            return redirect('recuperacion3')
        else:
            messages.error(request, 'El código de verificación no es válido.')
            return redirect('recuperacion2')
    return render(request, 'menu/recuperacion2.html')

def recuperacion3(request):
    if request.method == 'POST':
        nueva_contraseña = request.POST['nueva-contraseña']
        confirmar_contraseña = request.POST['confirmar-contraseña']
        if nueva_contraseña == confirmar_contraseña:
            correo = request.session.get('correo')
            usuario = Usuario.objects.filter(correo=correo).first()
            if usuario:
                usuario.contrasena = nueva_contraseña
                usuario.save()
                messages.success(request, 'Contraseña actualizada exitosamente.')
                return redirect('index')
            else:
                messages.error(request, 'No se encontró ningún usuario con ese correo.')
                return redirect('recuperacion3')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('recuperacion3')
    return render(request, 'menu/recuperacion3.html')

@login_required
def form(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        rut = request.POST.get('rut')
        titular = request.POST.get('titular')
        numero_tarjeta = request.POST.get('numero_tarjeta')
        codigo_seguridad = str(request.POST.get('codigo_seguridad'))
        fecha_vencimiento = request.POST.get('fecha_vencimiento')

        # Crear una nueva instancia de Tarjeta y asignar los valores
        tarjeta = Tarjeta.objects.create(
            rut=rut,
            titular=titular,
            numero_tarjeta=numero_tarjeta,
            codigo_seguridad=codigo_seguridad,
            fecha_vencimiento=fecha_vencimiento
        )

        # Asociar la tarjeta al usuario actualmente autenticado
        usuario = request.user
        usuario.tarjeta_id = tarjeta.id_tarjeta
        usuario.save()

        # Redirigir a una página de éxito o realizar otras acciones
        return redirect('form')

    return render(request, 'menu/form.html')



def carrito(request):
    if request.method == 'POST':
        comida_id = request.POST.get('comida_id')  # Obtener el ID del platillo seleccionado desde el formulario
        # Aquí debes implementar la lógica para agregar el platillo al carrito
        # Puedes almacenar los platillos en la sesión del usuario o en una base de datos

        # Por ejemplo, si las comidas agregadas se almacenan en la sesión del usuario
        carrito = request.session.get('carrito', [])  # Obtener las comidas del carrito desde la sesión
        carrito.append(comida_id)  # Agregar el ID del platillo seleccionado al carrito
        request.session['carrito'] = carrito  # Actualizar el carrito en la sesión

    comidas_agregadas = request.session.get('carrito', [])  # Obtener las comidas del carrito desde la sesión
    comidas = Comida.objects.filter(id_comida__in=comidas_agregadas)

    context = {'comidas': comidas}
    return render(request, 'menu/carrito.html', context)



def agregar_platillos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_platillo')
        descripcion = request.POST.get('descripcion_platillo')
        ingredientes = request.POST.get('ingredientes_platillo')
        foto = request.FILES['imagen_platillo']
        precio = request.POST.get('precio_platillo')
        especial = request.POST.get('especial_platillo') == 'on'  # Verifica si el checkbox está seleccionado

        comida = Comida(nombre=nombre, descripcion=descripcion, ingredientes=ingredientes, foto=foto, precio=precio,especial=especial)
        comida.save()
        
        
        return redirect('entorno')

    return render(request, 'menu/agregar_platillos.html')



def platillos(request):
    comidas = Comida.objects.all()
    context = {'comida': comidas}
    return render(request, 'menu/platillos.html', context)



def entorno(request):
    comidas = Comida.objects.filter(especial=True)
    context = {'comida': comidas}
    return render(request, 'menu/entorno.html', context)



def modificar_platillos(request):
    comidas = Comida.objects.all()
    context = {'comida': comidas}
    return render(request,'menu/modificar_platillos.html', context)

def modificar_form(request, pk):
    platillo = get_object_or_404(Comida, pk=pk)

    if request.method == 'POST':
        # Procesar los datos enviados en el formulario y guardar los cambios
        print("")
        # ...     
    else:
        context = {
            'platillo': platillo,
        }
        return render(request, 'menu/modificar_form.html', context)



def eliminar_platillos(request):
    if request.method == 'POST':
        platillo_id = int(request.POST['platillo_id'])
        Comida.objects.filter(id_comida=platillo_id).delete()
        return redirect('eliminar_platillos')
    
    platillos = Comida.objects.all()
    return render(request, 'menu/eliminar_platillos.html', {'platillos': platillos})



def perfil(request):
    return render(request,'menu/perfil.html')



def editar_perfil(request):
    return render(request, 'menu/editar_perfil.html',)

def editarperfil(request):
    # Obtener el objeto Usuario de la base de datos
    usuario = Usuario.objects.get(id_usuario=request.session['user_id'])
    
    if request.method == 'POST':
        # Actualizar los campos del perfil con los valores ingresados por el usuario
        usuario.nombre = request.POST.get('apodo')
        usuario.direccion = request.POST.get('direccion')
        usuario.telefono = request.POST.get('telefono')
        usuario.foto = request.FILES.get('foto-perfil')
        usuario.save()
        
        # Actualizar la variable de sesión con los nuevos valores
        request.session['user_nombre'] = usuario.nombre
        request.session['user_telefono'] = usuario.telefono
        request.session['user_direccion'] = usuario.direccion
        request.session['user_foto'] = usuario.foto.url if usuario.foto else ''
    
    return render(request, 'menu/perfil.html')

def pas_nuevo_usuario(request):
    return render(request,'menu/pas_nuevo_usuario.html')

def crearnombre(request):
    return render(request, 'menu/crearnombre.html')

def mi_formulario(request):
    if request.method == 'POST':
        # Procesar los datos enviados por el formulario
        contrasena = request.POST.get('contraseña')
        confi_contrasena = request.POST.get('confi-contraseña')
        
        return render(request, 'menu/crearnombre.html')
    else:
        return render(request, 'menu/pas_nuevo_usuario.html')



def val_nuevo_usuario(request):
    return render(request,'menu/val_nuevo_usuario.html')


"""
def validacion_nuevo_usuario(request):
    
    if request.method == 'POST':
        # Procesa los datos del formulario de validación de correo
        codigo_correo = request.POST.get('codigo_correo_nuevo_usuario')
        
        
        
    return render(request, 'val_nuevo_usuario.html')
"""



def nosotros(request):
    return render(request,'menu/nosotros.html')


def cambiar_contra(request):
    return render(request, 'menu/cambiar_contra.html')

def crear_usuario(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        if codigo == request.session.get('codigo_correo'):
            nombre = request.session.get('nombre')
            email = request.session.get('email')
            direccion = request.session.get('direccion')
            telefono = request.session.get('telefono')
            contrasena = request.session.get('contrasena')

            # Cifrar la contraseña utilizando make_password
            contrasena_cifrada = make_password(contrasena)

            usuario = Usuario(nombre=nombre, correo=email, telefono=telefono, contrasena=contrasena_cifrada, direccion=direccion)
            usuario.save()

            # Limpiar los datos de la sesión
            request.session.pop('codigo_correo', None)
            request.session.pop('email', None)
            request.session.pop('nombre', None)
            request.session.pop('direccion', None)
            request.session.pop('telefono', None)
            request.session.pop('contrasena', None)

            # Mostrar un mensaje de éxito
            messages.success(request, 'Usuario creado exitosamente.')

            return redirect('index')
        else:
            # Mostrar un mensaje de error si el código de validación es incorrecto
            messages.error(request, 'El código de validación es incorrecto.')
            return redirect('crear_usuario')

    return render(request, 'val_nuevo_usuario.html')

def crearnombreusuario(request):
    if not request.session.get('codigo_validado'):
        return redirect('index')

    if request.method == 'POST':
        
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']

        # Crear un nuevo usuario en la base de datos
        nuevo_usuario = Usuario(
            nombreusuario=nombre,
            telefonousuario=telefono,
            direccion_id=direccion,
        )
        nuevo_usuario.save()
        return redirect('entorno')
    else:
        return render(request, 'menu/index.html')
    
def iniciar_sesion(request):
    return render(request, 'menu/index.html')
    



def cerrar_sesion(request):
    logout(request)
    return redirect('index')

# def recupcontra(request):
#     if request.method == 'POST':
#         correo = request.POST['email']
#         usuario = Usuario.objects.filter(correo=correo).first()
#         if usuario:
#             codigo_verificacion = generar_codigo_verificacion()
#             # Envío de correo electrónico con el código de verificación
#             enviar_correo_recuperacion(correo, codigo_verificacion)
#             # Almacenar el código de verificación en la sesión del usuario
#             request.session['codigo_verificacion'] = codigo_verificacion
#             request.session['correo'] = correo
#             return redirect('recuperacion2')
#         else:
#             messages.error(request, 'No se encontró ningún usuario con ese correo.')
#             return redirect('recupcontra')
#     return render(request, 'menu/recuperacion.html')

def generar_codigo_verificacion():
    # Generar un código de verificación de 8 dígitos
    return '-'.join(str(random.randint(1000, 9999)) for _ in range(2))

def enviar_correo_recuperacion(correo, codigo_verificacion):
    # Código para enviar el correo de recuperación a la dirección de correo electrónico proporcionada
    # Aquí puedes utilizar la función send_mail() de Django o cualquier otra biblioteca para enviar correos electrónicos
    # Ejemplo utilizando send_mail():
    subject = 'Recuperación de contraseña'
    message = f'Tu código de verificación es: {codigo_verificacion}'
    send_mail(subject, message, 'noreply@example.com', [correo])