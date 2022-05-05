from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from women.models import *


menu = ['Main Page', 'About site', 'Add bookmark', 'Back answer']


def index(request):  # HttpRequest
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts,
                                                'menu': menu,
                                                'title': 'MAIN PAGE'})


def about(request):  # HttpRequest
    return render(request, 'women/about.html', {'menu': menu,
                                                'title': 'ABOUT SITE'})


def categories(request, catid):  # HttpRequest
    print(request.GET)
    return HttpResponse(f'<h1>Texts</h1><p>{catid}</p>')


def archive(request, year):  # HttpRequest
    CURRENT_YEAR = 2022
    if int(year) > CURRENT_YEAR:
        return redirect('home', permanent=True)
        # raise Http404()
    return HttpResponse(f'<h1>Archive for years</h1><p>{year}</p>')


def pageNotFound(request, exception):  # HttpRequest
    return HttpResponseNotFound(f'<h1>Error_404</h1>')
