from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from inventario.models import Producto
from inventario.forms import ProductoForm



# Create your views here.
def inicio(request):
	return render_to_response('login.html', context_instance=RequestContext(request))

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
