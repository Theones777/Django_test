from django import forms
from women.models import *


class AddFormPost(forms.Form):
    title = forms.CharField(max_length=255,
                            label='Заголовок',
                            widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60,
                                                           'rows': 10}))
    is_published = forms.BooleanField(required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 empty_label='Category not chosen')

