
from django.urls import path
from . import views

urlpatterns = [
    #Home
    path('',  views.bloghome , name='bloghome'),

    #Auth
    path('signup/',  views.signupuser, name='signupuser'),
    path('login/',  views.loginuser , name='loginuser'),
    path('logout/',  views.logoutuser , name='logoutuser'),

    #ShowBlogPage
    path('bloglist-<str:blog_category>/',  views.bloglist , name='bloglist'),
    path('detailedblogs/<int:blog_id>',  views.detailedblogs , name='detailedblog'),

    #WriteBlogPage
    path('writeblog/',  views.writeblog , name='writeblog'),

    #DetailedVocab
    path('individualvocab-<str:vocab>/',  views.individualvocab , name='individualvocab'),

    #LikesCount
    path('likescount', views.likescount, name = 'likescount'),

    #Comment
    path('comment', views.comment, name='comment'),

    #Reply
    path('reply', views.reply, name='reply')


]
