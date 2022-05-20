from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from women.forms import *
from women.models import *
from women.utils import *


class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Main Page')
        return context | c_def

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


# def index(request):  # HttpRequest
#     posts = Women.objects.all()
#
#     context = {'posts': posts,
#                'menu': menu,
#                'title': 'MAIN PAGE',
#                'cat_selected': 0}
#
#     return render(request, 'women/index.html', context=context)

# @login_required   # 403 access denied
def about(request):  # HttpRequest
    return render(request, 'women/about.html', {'menu': menu,
                                                'title': 'ABOUT SITE'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddFormPost
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True  # 403 access denied

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Dobavlenie stat'i")
        return context | c_def


# def addpage(request):  # HttpRequest
#     if request.method == 'POST':
#         form = AddFormPost(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()   # Women.objects.create(**form.cleaned_data)
#             return redirect('home')
#     else:
#         form = AddFormPost()
#     return render(request, 'women/addpage.html',
#                   {'form': form, 'menu': menu, 'title': "Dobavlenie stat'i"})


def contact(request):  # HttpRequest
    return HttpResponse('Contacts')


def login(request):  # HttpRequest
    return HttpResponse('Log in')


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return context | c_def


# def show_post(request, post_slug):  # HttpRequest
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {'post': post,
#                'menu': menu,
#                'title': post.title,
#                'cat_selected': post.cat_id}
#
#     return render(request, 'women/post.html', context=context)


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False  # for 404 error

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return context | c_def

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                    is_published=True)


# def show_category(request, cat_id):  # HttpRequest
#     posts = Women.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#     context = {'posts': posts,
#                'menu': menu,
#                'title': 'CATEGORY PAGE',
#                'cat_selected': cat_id}
#
#     return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):  # HttpRequest
    return HttpResponseNotFound(f'<h1>Error_404</h1>')
