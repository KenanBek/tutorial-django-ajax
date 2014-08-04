from django.http import HttpResponse
from django.shortcuts import render


def index(request, template='sample1/index.html', context={}):
    return render(request, template, context)


def hello(request):
    return HttpResponse('Hello Client!')
