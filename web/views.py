from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf

def login_user(request):
	c = { }
	c.update(csrf(request)) # pass in true html template
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login_user(request, user)
		return HttpResponseRedirect('/anasayfa')
	else:
		return HttpResponseRedirect('/invalid')
	
def anasayfa(request):
	return render_to_response('anasayfa.html')
				
def invalid(request):
	return render_to_response('invalid.html')
	
