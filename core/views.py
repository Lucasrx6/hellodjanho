from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome):
    return HttpResponse ('<H1>Hello World, valeu () <H1>'.format(nome))