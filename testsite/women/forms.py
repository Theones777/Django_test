from django import forms
from django.core.exceptions import ValidationError

from women.models import *


class AddFormPost(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'No chosen category'

    class Meta:
        model = Women
        fields = ['title', 'content', 'slug', 'cat', 'is_published', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60,
                                             'rows': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 20:
            raise ValidationError('Too much length')
        return title

