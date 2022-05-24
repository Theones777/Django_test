from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
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
        return Women.objects.filter(is_published=True).select_related('cat')


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
    contact_list = Women.objects.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'women/about.html', {'page_obj': page_obj,
                                                'menu': menu,
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
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Category - ' + str(c.name),
                                      cat_selected=c.pk)
        return context | c_def

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                    is_published=True).select_related('cat')


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


def logout_user(request):
    logout(request)
    return redirect('login')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Registration')
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Autorisation')
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'women/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Back answer')
        return context | c_def

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')
