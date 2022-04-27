from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):  # HttpRequest
    return HttpResponse('Страница приложения women')


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