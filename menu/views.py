from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuario,Comida
from django.core.mail import send_mail
from django.conf import settings
from random import randint
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'menu/index.html')


def login(request):
    if request.method == 'POST':
        # Procesa los datos del formulario de inicio de sesión
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Verifica las credenciales del usuario en la base de datos
        try:
            usuario = Usuario.objects.get(correo=email, clave=password)
        except Usuario.DoesNotExist:
            response = redirect('index')
            response.set_cookie('error_message', 'Correo o contraseña incorrectos')
            return response
        
        return redirect('entorno')  # Redirige a la página de entorno.html después del inicio de sesión exitoso
    
    error_message = request.COOKIES.get('error_message')
    response = render(request, 'index.html', {'error_message': error_message})
    response.delete_cookie('error_message')
    return response

"""

def register(request):
    if request.method == 'POST':
        # Procesa los datos del formulario de registro
        #usuario=usuari
        email = request.POST.get('email')
        
        
    return render(request, 'index.html')
"""
def registro(request):
    return render(request,'menu/registro.html')


def entorno(request):
    return render(request,'menu/entorno.html')

def recuperacion(request):
    return render(request,'menu/recuperacion.html')

def recuperacion2(request):
    return render(request,'menu/recuperacion2.html')

def recuperacion3(request):
    return render(request,'menu/recuperacion3.html')

def form(request):
    return render(request,'menu/form.html')

def carrito(request):
    comidas = Comida.objects.all()
    context = {'comidas': comidas}
    return render(request, 'menu/carrito.html', context)

def agregar_platillos(request):
    
    return render(request,'menu/agregar_platillos.html')

def platillos(request):
    comidas = Comida.objects.all()
    context = {'comida': comidas}
    return render(request, 'menu/platillos.html', context)

def entorno(request):
    comidas = Comida.objects.filter(especial=True)
    context = {'comida': comidas}
    return render(request, 'menu/entorno.html', context)


def eliminar_platillos(request):
    platillos = Comida.objects.all()
    context = {
        'platillos': platillos
    }
    return render(request, 'menu/eliminar_platillos.html', context)

def perfil(request):
    return render(request,'menu/perfil.html')

def editar_perfil(request):
    return render(request,'menu/editar_perfil.html')

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


def register(request):
    if request.method == 'POST':
        print("1111111111111")
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
            return redirect('val_nuevo_usuario')
        
        return render(request, 'menu/index.html')


def validacion_nuevo_usuario(request):
    if request.method == 'POST':
        codigo_ingresado = request.POST.get('codigo_correo_nuevo_usuario')
        email = request.session.get('email')
        codigo_correo = request.session.get('codigo_correo')

        if codigo_ingresado == codigo_correo:
            # El código de validación es correcto
            request.session['codigo_validado'] = True
            return redirect('pas_nuevo_usuario')
        else:
            # El código de validación es incorrecto
            error_message = 'Código de validación incorrecto'
            return render(request, 'val_nuevo_usuario.html', {'error_message': error_message})
    else:
        # Si el método de solicitud no es POST, redirige a la página anterior
        return redirect('val_nuevo_usuario')


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