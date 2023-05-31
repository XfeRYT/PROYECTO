from django.db import models
from django.utils.translation import gettext_lazy as _
from ventas.models import Venta
from compras.models import Compra
from producto.models import Producto
# Create your models here.
class Detalle_Venta(models.Model):
    nombre=models.ForeignKey(Producto, verbose_name=_("Nombre"), on_delete=models.CASCADE)
    cantidad=models.IntegerField(max_length=45,verbose_name="Cantidad")
    venta=models.ForeignKey(Venta, verbose_name=_("Venta"), on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=45,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    
    def __str__(self):
        return "%s"%(self.nombre)
    class Meta:
        verbose_name_plural = "Detalles de ventas"

class Detalle_Compra(models.Model):
    producto=models.ForeignKey(Producto, verbose_name="Nombre", on_delete=models.CASCADE)
    precio_compra=models.PositiveIntegerField(max_length=45,verbose_name="Precio de compra")
    precio_venta=models.PositiveIntegerField(max_length=45,verbose_name="Precio de venta")
    compra=models.ForeignKey(Compra, verbose_name=_("Compra"), on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=45,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    
    def __str__(self):
        return "%s"%(self.producto)
    class Meta:
        verbose_name_plural = "Detalles de compras"
class Stock(models.Model):
    cantidad=models.SmallIntegerField(max_length=45,verbose_name="Cantidad")
    detalle_venta=models.ForeignKey(Detalle_Venta, verbose_name=_("Detalle venta"), on_delete=models.CASCADE)
    detalle_compra=models.ForeignKey(Detalle_Compra, verbose_name=_("Detalle compra"), on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=45,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    
    def __str__(self):
        return "%s"%(self.cantidad)
    class Meta:
        verbose_name_plural = "Stocks"