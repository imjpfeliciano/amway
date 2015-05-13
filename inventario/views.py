from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from inventario.models import Producto
from inventario.forms import ProductoForm, ReporteForm, UsuarioForm, LoginForm, UserForm
from django.contrib.auth.decorators import user_passes_test



# Create your views here.
def validar_admin(user):
	return user.is_staff

def validar_user(user):
	return not user.is_staff and user.is_active

def inicio(request):
	if request.method == 'POST':
		formulario = LoginForm(request.POST)
		print formulario
		if formulario.is_valid():
			#usuario = Usuarios.objects.get(nombre_usuario__exact=formulario.cleaned_data['nombre_usuario'])
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					if acceso.is_staff:
						return HttpResponseRedirect('admin/')
					else:
						return HttpResponseRedirect('user/')				
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	return render_to_response('login.html',context_instance=RequestContext(request))

@user_passes_test(validar_admin, login_url="/")
def admin_index(request):
	return render_to_response('admin/menu.html', context_instance=RequestContext(request))

@user_passes_test(validar_user, login_url="/")
def user_index(request):
	return render_to_response('user/menu.html', context_instance=RequestContext(request))

@login_required(login_url="/")
def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect("/")



@user_passes_test(validar_admin)
def nuevo_usuario(request):
	if request.method == 'POST':
		formulario = UsuarioForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/admin')
	else:
		formulario = UsuarioForm()
	return render_to_response('admin/nuevo_usuario.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url="/")
def lista_productos(request):
	productos = Producto.objects.all()
	return render_to_response('inventario.html', {'lista':productos}, context_instance=RequestContext(request))

@user_passes_test(validar_admin)
def nuevo_producto(request):
	if request.method == 'POST':
		formulario = ProductoForm(request.POST, request.FILES)
		if formulario.is_valid():
			#print "correcto"
			formulario.save()
			return HttpResponseRedirect('../inventario/')
	else:
		formulario = ProductoForm()
		return render_to_response('admin/nuevo_producto.html', {'formulario':formulario}, context_instance=RequestContext(request))

def crear_ticket(request):
	return render_to_response('user/ticket.html', context_instance=RequestContext(request))

def ver_reporte(request):
	return render_to_response('admin/reportes.html')
