from django.db import models
from usuarios.models import Usuario
from django.utils.translation import gettext_lazy as _

# Create your models here.

        
class Cuenta_Pendiente(models.Model):
    nombre=models.CharField(max_length=45,verbose_name="Nombre")
    fecha_inicio=models.DateField(verbose_name="Fecha de Inicio", help_text="MM/DD/AAAA", auto_now=True)
    valor=models.IntegerField(max_length=45,verbose_name="Valor")
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=15,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s"%(self.nombre)
    class Meta:
        verbose_name_plural = "Cuentas Pendientes"


class Compra(models.Model):
    fecha=models.DateField(verbose_name="Fecha", help_text="MM/DD/AAAA", auto_now=True)
    idusuario=models.ForeignKey(Usuario, verbose_name=_("Usuario"), on_delete=models.CASCADE)
    idcuentapendiente=models.ForeignKey(Cuenta_Pendiente, verbose_name=_("Cuenta Pendiente"), on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=15,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s %s"%(self.fecha,self.estado)
    class Meta:
        verbose_name_plural = "Compras"