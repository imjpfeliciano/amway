from django.forms import ModelForm
from django import forms
from inventario.models import Producto, Reporte, Usuario

class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		fields = '__all__'

class ReporteForm(ModelForm):
	class Meta:
		model = Reporte
		fields = '__all__'

class UsuarioForm(ModelForm):
	class Meta:
		model = Usuario
		fields = '__all__'