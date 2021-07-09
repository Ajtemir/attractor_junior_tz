from django import forms
from blog.models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ['user', 'create', 'uploaded']
