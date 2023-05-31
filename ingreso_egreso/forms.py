from django import forms
from django.forms import ModelForm, widgets
from ingreso_egreso.models import Detalle_Venta
from ingreso_egreso.models import Detalle_Compra
from ingreso_egreso.models import Stock



class StockForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields = "__all__"
        exclude=["estado"]
class StockUpdateForm(ModelForm):
    
    class Meta:
        model = Stock
        fields = "__all__"
        exclude=["estado"]
        
class Detalle_CompraForm(forms.ModelForm):
    class Meta:
        model=Detalle_Compra
        fields = "__all__"
        exclude=["estado"]
class Detalle_CompraUpdateForm(ModelForm):
    
    class Meta:
        model = Detalle_Compra
        fields = "__all__"
        exclude=["estado"]
        
class Detalle_VentaForm(forms.ModelForm):
    class Meta:
        model=Detalle_Venta
        fields = "__all__"
        exclude=["estado"]
class Detalle_VentaUpdateForm(ModelForm):
    
    class Meta:
        model = Detalle_Venta
        fields = "__all__"
        exclude=["estado"]