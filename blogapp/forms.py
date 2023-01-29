from dataclasses import fields
from django.forms import ModelForm
from .models import Article, Vocab

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'title', 'short_description', 'content']

class VocabForm(ModelForm):
    class Meta:
        model = Vocab
        fields = ['voc']

