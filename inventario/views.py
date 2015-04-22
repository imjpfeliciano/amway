from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.contrib.auth.decorators import login_required



# Create your views here.
def inicio(request):
	return render_to_response('login.html', context_instance=RequestContext(request))

#@login_required(login_url='/inicio')
def test(request):
	return render_to_response('test.html', context_instance=RequestContext(request))
