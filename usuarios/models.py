from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=45,verbose_name="Nombre", unique=True)
    apellido=models.CharField(max_length=45,verbose_name="Apellido")
    contraseña=models.CharField(max_length=45,verbose_name="Contraseña")
    class TipoDocumento(models.TextChoices):
        CEDULA='CC',_("Cédula")
        TARJETA='TI',_("Tarjeta de Identidad")
        CEDULA_EXTRANJERIA='CE',_("Cédula de Extrangería")
    tipo_documento=models.CharField(max_length=2,choices=TipoDocumento.choices,verbose_name="Tipo de Documento")
    documento=models.CharField(max_length=45,verbose_name="Documento")
    telefono=models.CharField(max_length=45,verbose_name="Telefono")
    direccion=models.CharField(max_length=45,verbose_name="Dirección")
    correo=models.CharField(max_length=45,verbose_name="Correo")
    class Rol(models.TextChoices):
        ADMIN='Admin',_("Administrador")
        EMPLEADO='Empleado',_("Empleado")
        USUARIO='Usuario',_("Usuario")
    rol=models.CharField(max_length=10,choices=Rol.choices,verbose_name="Rol")
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=45,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s %s"%(self.nombre, self.apellido)
    class Meta:
        verbose_name_plural = "Usuarios"

class Sucursal(models.Model):
    nombre = models.CharField(max_length=45,verbose_name="Nombre")
    direccion=models.CharField(max_length=45,verbose_name="Dirección")
    municipio=models.CharField(max_length=45,verbose_name="Municipio")
    telefono=models.CharField(max_length=45,verbose_name="Telefono")
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=45,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s %s"%(self.nombre,self.municipio)
    class Meta:
        verbose_name_plural = "Sucursales"
class Usuario_has_Sucursal(models.Model):
    idusuario=models.ForeignKey(Usuario, verbose_name=_("ID Usuario"), on_delete=models.CASCADE)
    idsucursal=models.ForeignKey(Sucursal, verbose_name=_("ID Sucursal"), on_delete=models.CASCADE)