from email.policy import default
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class CategoryClass(models.Model):
    category = models.CharField(max_length = 100)

    def __str__(self):
        return self.category

# article_category_choices = (('Not Sure', 'Not Sure'),('Technology','Technology'), ('Math','Math'))
# article_category_choices = (list(CategoryClass.objects.all().values()))
# choice_tuple = ()
# for i in article_category_choices:
#     choice_tuple = choice_tuple + ((i['category'], i['category']),)


class Article(models.Model):
    # category = models.CharField(max_length = 100, choices = choice_tuple, default = 'Not Sure')
    category = models.ForeignKey(CategoryClass, on_delete = models.CASCADE, default = True)
    title = models.CharField(max_length = 200)
    short_description = models.CharField(max_length = 1000)
    # content = models.TextField()
    content = RichTextField()
    time_modified = models.DateTimeField(auto_now = True)
    time_created = models.DateTimeField(auto_now_add = True)
    approved = models.BooleanField(default= False)
    contributor = models.ForeignKey(User, on_delete = models.CASCADE, default=User.objects.get(username = 'vatsa').pk)
    likes = models.IntegerField(default=0)
    liked_user = models.ManyToManyField(User, related_name= 'user')



    def __str__(self):
        return "Category: " + str(self.category) +  " & Title: " + self.title

class Vocab(models.Model):
    article_title = models.ForeignKey(Article, on_delete = models.CASCADE, default = True)
    voc = models.TextField(default = "")

    def __str__(self):
        return "Vocab for Article Title: " + str(self.article_title)
    




    













# class fi(models.Model):
#     fs = models.FileField()
#     imdir = models.ImageField()
#     title = models.TextField()

#     def __str__(self):
#         return self.title
