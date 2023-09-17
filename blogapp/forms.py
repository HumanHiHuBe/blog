from dataclasses import fields
from django import forms
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
        labels = {
            'comment_text' : "Add comments on this post"
        }
        widgets = {
            'comment_text': forms.TextInput(attrs={'placeholder': 'Add Comment'}),
        }
        
class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['reply_text']
        labels = {
            'reply_text' : "Reply to above comment"
        }
        widgets = {
            'reply_text': forms.TextInput(attrs={'placeholder': 'Reply'}),
        }

