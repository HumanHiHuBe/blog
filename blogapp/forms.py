from dataclasses import fields
from django.forms import ModelForm
from .models import Article, Vocab, Comment, Reply

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'title', 'short_description', 'content']

class VocabForm(ModelForm):
    class Meta:
        model = Vocab
        fields = ['voc']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['reply_text']

