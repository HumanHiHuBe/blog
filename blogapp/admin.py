from django.contrib import admin
from .models import Article, CategoryClass, Vocab

# Register your models here.

admin.site.register(Article)
admin.site.register(CategoryClass)
admin.site.register(Vocab)


