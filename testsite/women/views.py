from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from women.models import *

menu = [{'title': 'About site', 'url_name': 'about'},
        {'title': 'Add page', 'url_name': 'add_page'},
        {'title': 'Back answer', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'}]


def index(request):  # HttpRequest
    posts = Women.objects.all()
    cats = Category.objects.all()

    context = {'posts': posts,
               'cats': cats,
               'menu': menu,
               'title': 'MAIN PAGE',
               'cat_selected': 0}

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


def show_category(request, cat_id):  # HttpRequest
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()
    context = {'posts': posts,
               'cats': cats,
               'menu': menu,
               'title': 'CATEGORY PAGE',
               'cat_selected': cat_id}

    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):  # HttpRequest
    return HttpResponseNotFound(f'<h1>Error_404</h1>')
