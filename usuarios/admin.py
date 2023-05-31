from django.contrib import admin
from usuarios.models import Usuario
from usuarios.models import Sucursal
from usuarios.models import Usuario_has_Sucursal


# Register your models here.
admin.site.register(Usuario)
admin.site.register(Sucursal)
admin.site.register(Usuario_has_Sucursal)

