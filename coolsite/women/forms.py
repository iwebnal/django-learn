from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    # title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))
    # slug = forms.SlugField(max_length=255, label="URL")
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Текст")
    # is_published = forms.BooleanField(label="Публикация", required=False, initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label="Категория не выбрана")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # run constructor base class
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Women  # connect with model
        # fields = '__all__'  # connect with model fields
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']  # connect with model fields
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
