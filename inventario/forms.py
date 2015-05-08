from django.forms import ModelForm
from django import forms
from inventario.models import Producto, Reporte, Usuario, Login

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

class LoginForm(ModelForm):
	class Meta:
		model = Login
		fields = '__all__'