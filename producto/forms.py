from django import forms
from django.forms import ModelForm, widgets
from producto.models import Marca
from producto.models import Producto
from producto.models import Unidades
from producto.models import Subcategoria
from producto.models import Categoria



class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields = "__all__"
        exclude=["estado"]
class ProductoUpdateForm(ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
        exclude=["estado"]
        
class MarcaForm(forms.ModelForm):
    class Meta:
        model=Marca
        fields = "__all__"
        exclude=["estado"]
class MarcaUpdateForm(ModelForm):
    class Meta:
        model = Marca
        fields = "__all__"
        exclude=["estado"]

class UnidadesForm(forms.ModelForm):
    class Meta:
        model=Unidades
        fields = "__all__"
        exclude=["estado"]
        
class UnidadesUpdateForm(ModelForm):
    class Meta:
        model = Unidades
        fields = "__all__"
        exclude=["estado"]

class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model=Subcategoria
        fields = "__all__"
        exclude=["estado"]
class SubcategoriaUpdateForm(ModelForm):
    class Meta:
        model = Subcategoria
        fields = "__all__"
        exclude=["estado"]
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields = "__all__"
        exclude=["estado"]
class CategoriaUpdateForm(ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"
        exclude=["estado"]
        
