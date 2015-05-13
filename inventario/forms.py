from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from inventario.models import Producto, Reporte, Usuario, Login

class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		fields = '__all__'

class ReporteForm(ModelForm):
	class Meta:
		model = Reporte
		fields = '__all__'

class UsuarioForm(UserCreationForm):
	first_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('username','first_name','email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(UsuarioForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()
		return user

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class LoginForm(ModelForm):
	class Meta:
		model = Login
		fields = '__all__'