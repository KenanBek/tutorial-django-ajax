from django.shortcuts import render


def index(request, template="sample2/index.html", context={}):
    return render(request, template, context)
