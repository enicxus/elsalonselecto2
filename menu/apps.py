from django.apps import AppConfig

#define una nueva clase de MenuConfig que hereda de AppConfig
class MenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu'
