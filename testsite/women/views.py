from django.shortcuts import render
from django.http import HttpResponse


def index(request):  # HttpRequest
    return HttpResponse('Страница приложения women')


def categories(request):  # HttpRequest
    return HttpResponse('<h1>States</h1>')
