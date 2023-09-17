from email.policy import default
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class CategoryClass(models.Model):
    category = models.CharField(max_length = 100, unique=True)
    def __str__(self):
        return self.category


class Article(models.Model):
    category = models.ForeignKey(CategoryClass, on_delete = models.CASCADE, default = True)
    title = models.CharField(max_length = 200, unique=True)
    short_description = models.CharField(max_length = 1000)
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
    
class Comment(models.Model):
    article_tit = models.ForeignKey(Article, on_delete = models.CASCADE)
    commented_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length = 10000)
    
    def __str__(self):
        return "Comment On Article: " + str(self.article_tit) + "Commented by : " + str(self.commented_user) + str(self.comment_text[:10])


class Reply(models.Model):
    original_comment = models.ForeignKey(Comment, on_delete = models.CASCADE)
    replying_user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_text = models.CharField(max_length = 10000)

    def __str__(self):
        return "Reply On Comment: " + str(self.original_comment) + "Replied by : " + str(self.replying_user) + str(self.reply_text[:10])