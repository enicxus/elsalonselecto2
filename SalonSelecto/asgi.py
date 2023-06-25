"""
ASGI config for SalonSelecto project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
#establece la configuracion del entorno para el proyecto django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SalonSelecto.settings')
#aplicaccion asgi configurada para el proyecto django
application = get_asgi_application()
