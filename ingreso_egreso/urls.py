from django.urls import path

from ingreso_egreso.views import stock_listar, stock_crear, stock_modificar, stock_eliminar
from ingreso_egreso.views import detalle_compra_listar, detalle_compra_crear, detalle_compra_modificar, detalle_compra_eliminar
from ingreso_egreso.views import detalle_venta_listar, detalle_venta_crear, detalle_venta_modificar, detalle_venta_eliminar


urlpatterns = [
    path('', stock_listar, name="stock" ),
    path('crear/', stock_crear, name="stock-crear" ),
    path('modificar/<int:pk>/', stock_modificar, name="stock-modificar" ),
    path('stock/eliminar/<int:pk>/', stock_eliminar, name="stock-eliminar" ),
    
    
    path('detalle_compra/', detalle_compra_listar, name="detalle_compra" ),
    path('detalle_compra/crear/', detalle_compra_crear, name="detalle_compra-crear" ),
    path('detalle_compra/modificar/<int:pk>/', detalle_compra_modificar, name="detalle_compra-modificar" ),
    path('detalle compra/eliminar/<int:pk>/', detalle_compra_eliminar, name="detalle_compra-eliminar" ),

    path('detalle_venta/', detalle_venta_listar, name="detalle_venta" ),
    path('detalle_venta/crear/', detalle_venta_crear, name="detalle_venta-crear" ),
    path('detalle_venta/modificar/<int:pk>/', detalle_venta_modificar, name="detalle_venta-modificar" ),
    path('detalle venta/eliminar/<int:pk>/', detalle_venta_eliminar, name="detalle_venta-eliminar" ),

]
