from django.db.models import Count

from women.models import *

menu = [{'title': 'About site', 'url_name': 'about'},
        {'title': 'Add page', 'url_name': 'add_page'},
        {'title': 'Back answer', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('women'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
