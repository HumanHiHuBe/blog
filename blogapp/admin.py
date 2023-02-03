from django.contrib import admin
from .models import Article, CategoryClass, Vocab, Comment, Reply

# Register your models here.

admin.site.register(Article)
admin.site.register(CategoryClass)
admin.site.register(Vocab)
admin.site.register(Comment)
admin.site.register(Reply)


