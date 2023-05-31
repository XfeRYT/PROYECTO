from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'
class SucursalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sucursal'
class Usuario_has_SucursalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuario_has_sucursal'
