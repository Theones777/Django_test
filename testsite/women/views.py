from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from women.models import *

menu = [{'title': 'About site', 'url_name': 'about'},
        {'title': 'Add page', 'url_name': 'add_page'},
        {'title': 'Back answer', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'}]


def index(request):  # HttpRequest
    posts = Women.objects.all()
    context = {'posts': posts,
               'menu': menu,
               'title': 'MAIN PAGE'}
    return render(request, 'women/index.html', context=context)


def about(request):  # HttpRequest
    return render(request, 'women/about.html', {'menu': menu,
                                                'title': 'ABOUT SITE'})


def addpage(request):  # HttpRequest
    return HttpResponse('Add Page')


def contact(request):  # HttpRequest
    return HttpResponse('Contacts')


def login(request):  # HttpRequest
    return HttpResponse('Log in')


def show_post(request, post_id):  # HttpRequest
    return HttpResponse(f'Page with id = {post_id}')


def pageNotFound(request, exception):  # HttpRequest
    return HttpResponseNotFound(f'<h1>Error_404</h1>')
