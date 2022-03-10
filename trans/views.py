from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.http import HttpResponse
from .models import links

# Create your views here.


def home(request):
	value = request.user
	return render(request, 'home.html', { 'value':value})

def good(request, key):
	obj = links.objects.get(key=key)
	value = obj.value
	a="http://google.com"

	return HttpResponseRedirect(a)
	# return redirect('www.google.com')
	# return HttpResponse(f"You are goood : {value}" )
