from django.forms import ModelForm
from django import forms
from inventario.models import Producto

class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		fields = '__all__'