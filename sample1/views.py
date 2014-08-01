from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.

def index(request):
    return render_to_response('sample1/index.html', {'message': 'Hello World!'})

def hello(request):
    return HttpResponse('Hello Client!')
