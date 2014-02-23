from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf


def login_user(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login_user(request, user)
		return HttpResponseRedirect('/gramafon')
	else:
		return HttpResponseRedirect('/login')	
def gramafon(request):
	return render_to_response('homepage.html')
				
	
