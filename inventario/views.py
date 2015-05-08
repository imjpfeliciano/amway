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
from inventario.forms import ProductoForm, ReporteForm, UsuarioForm



# Create your views here.
def inicio(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid():
			#usuario = Usuarios.objects.get(nombre_usuario__exact=formulario.cleaned_data['nombre_usuario'])
			usuario = request.POST['username']
			clave = request.POST['password']
			print usuario, clave
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/valida')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('login.html', {'formulario':formulario},context_instance=RequestContext(request))

def nuevo_usuario(request):
	if request.method == 'POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()
	return render_to_response('nuevousuario.html', {'formulario':formulario}, context_instance=RequestContext(request))

#@login_required(login_url='/inicio')
def test(request):
	return render_to_response('test.html', context_instance=RequestContext(request))

def productos(request):
	formulario = ProductoForm()
	return render_to_response('producto_nuevo.html', {'formulario': formulario}, context_instance=RequestContext(request))

def lista_productos(request):
	productos = Producto.objects.all()
	return render_to_response('inventario.html', {'lista':productos}, context_instance=RequestContext(request))

def nuevo_producto(request):
	if request.method == 'POST':
		formulario = ProductoForm(request.POST, request.FILES)
		if formulario.is_valid():
			#print "correcto"
			formulario.save()
			return HttpResponseRedirect('/inventario')
	else:
		formulario = ProductoForm()
		return render_to_response('producto_nuevo.html', {'formulario':formulario}, context_instance=RequestContext(request))