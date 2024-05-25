from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Article, CategoryClass, Vocab, Comment, Reply
from .forms import ArticleForm, VocabForm, CommentForm, ReplyForm
from django.contrib.auth.decorators import login_required
from .function import function_to_render_correct_word_meaning, word_dictionary
from django.core.paginator import Paginator

# Create your views here.

#Home View
def bloghome(request):
    blog_category = CategoryClass.objects.all().order_by('category')
    pag = Paginator(blog_category, 5)
    page_number = request.GET.get('page')
    page_obj = pag.get_page(page_number)
    return render(request, 'blogapp/bloghome.html', {'page_obj' : page_obj})

#Auth Views
def signupuser(request):
    if request.method == 'GET': 
        return render(request, 'blogapp/signupuser.html', {'form':UserCreationForm()})
    else:
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            user = userform.save(commit=False)
            user.save()
        else:
            return render(request, 'blogapp/signupuser.html', {'form':UserCreationForm(), 'error':userform.errors})
    login(request, user)
    return redirect('bloghome')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'blogapp/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'blogapp/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('bloghome')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('bloghome')
    else:
        return HttpResponse("<h1>Forbidden</h1>")

#Articles Views 
def bloglist(request, blog_category):
    d = Article.objects.filter(category = CategoryClass.objects.get(category = blog_category)).order_by('-time_created', 'title')
    d = d.filter(approved = True)
    pag = Paginator(d, 5)
    page_number = request.GET.get('page')
    page_obj = pag.get_page(page_number)
    return render(request, 'blogapp/bloglist.html', {'page_obj' : page_obj, 'blog_category' : blog_category ,'count':d.count()})

def detailedblogs(request, blog_id):
    if request.method == 'GET':
        d = get_object_or_404(Article, pk=blog_id)
        com_form = CommentForm()
        rep_form = ReplyForm()
        likedUserList = d.liked_user.all()
        d1 = Vocab.objects.get(article_title = d)
        s = str(d1.voc)
        w = function_to_render_correct_word_meaning(s)
        w = w[0]
        coment_list = Comment.objects.filter(article_tit = d)
        newVar = 1
        if len(coment_list) == 0:
            newVar = 0

        final_list = []
        for i in coment_list:
            final_list.append([i, Reply.objects.filter(original_comment = i)])
        return render(request, 'blogapp/detailedblog.html', {'com_form':com_form, 'rep_form':rep_form, 'article':d, 'words': w, 'likedUserList':likedUserList, 'final_list':final_list, 'newVar':newVar})
    else:
        d = get_object_or_404(Article, pk=blog_id)
        com_form = CommentForm()
        rep_form = ReplyForm()
        likedUserList = d.liked_user.all()
        d1 = Vocab.objects.get(article_title = d)
        s = str(d1.voc)
        w = function_to_render_correct_word_meaning(s)
        w = w[0]
        coment_list = Comment.objects.filter(article_tit = d)
        newVar = 1
        if len(coment_list) == 0:
            newVar = 0
        final_list = []
        for i in coment_list:
            final_list.append([i, Reply.objects.filter(original_comment = i)])
        return render(request, 'blogapp/detailedblog.html', {'com_form':com_form, 'rep_form':rep_form, 'article':d, 'words': w, 'likedUserList':likedUserList, 'final_list':final_list, 'newVar':newVar})

#view for like habdling
def likescount(request):
    if request.POST:
        d = get_object_or_404(Article, pk=request.POST['article_id'])
        likedUserList = d.liked_user.all()
        if not request.user in likedUserList:
            d.likes = d.likes + 1
            d.liked_user.add(request.user)
        d.save()
        d = get_object_or_404(Article, pk=request.POST['article_id'])
        d1 = Vocab.objects.get(article_title = d)
        s = str(d1.voc)
        w = function_to_render_correct_word_meaning(s)
        w = w[0]
        likedUserList = d.liked_user.all()
        coment_list = Comment.objects.filter(article_tit = d)
        final_list = []
        for i in coment_list:
            final_list.append([i, Reply.objects.filter(original_comment = i)])
        com_form = CommentForm()
        rep_form = ReplyForm()
        return render(request, 'blogapp/detailedblog.html', {'com_form':com_form, 'rep_form':rep_form,'article':d, 'words': w, 'likedUserList':likedUserList, 'final_list':final_list})
    else:
        return HttpResponse("<h1>Forbidden</h1>")



#View for Detailed Vocab
def individualvocab(request, vocab):
    q = word_dictionary(vocab)
    return render(request, 'blogapp/individualvocab.html', {'res':q})


#View for writing blog
@login_required
def writeblog(request):
    if request.POST:
        form1 = ArticleForm(request.POST)
        if form1.is_valid():
            model1 = form1.save(commit= False)
            form2 = VocabForm(request.POST)
            if form2.is_valid():
                model2 = form2.save(commit=False)
                model2.article_title = model1
                model1.contributor = request.user
                if request.user.is_superuser or request.user.is_staff:
                    model1.approved = True
                w = function_to_render_correct_word_meaning(str(model2.voc))
                w = w[1]
                if len(w)>=1:
                    for i in range(len(w)):
                        model1.content = model1.content.replace(w[i], '<strong>'+w[i]+'</strong>')                                  
                        model1.content = model1.content.replace(w[i].lower(), '<strong>'+w[i]+'</strong>')                                  
                model1.save()
                model2.save()   
            else:
                return render(request, 'blogapp/writeblog.html', {'form1': ArticleForm(), 'form2':VocabForm(), 'msg': 'Field Error, Please correct and resubmit.'})
        else:
            return render(request, 'blogapp/writeblog.html', {'form1': ArticleForm(), 'form2':VocabForm(), 'msg': 'Field Error, Please correct and resubmit.'})
        return render(request, 'blogapp/writeblog.html', {'form1': ArticleForm(), 'form2':VocabForm(), 'msg': 'Saved Sucessfully.', 'model1':model1})
    else:
        return render(request, 'blogapp/writeblog.html', {'form1': ArticleForm(), 'form2':VocabForm(), 'msg':''})

def comment(request):
    if request.method == 'POST':
        cForm = CommentForm(request.POST)
        d = get_object_or_404(Article, pk=request.POST['com_article'])
        if cForm.is_valid():
            comModel = cForm.save(commit=False)
            comModel.commented_user = request.user
            comModel.article_tit = d
            comModel.save()
            com_form = CommentForm()
            rep_form = ReplyForm()
            likedUserList = d.liked_user.all()
            d1 = Vocab.objects.get(article_title = d)
            s = str(d1.voc)
            w = function_to_render_correct_word_meaning(s)
            w = w[0]
            coment_list = Comment.objects.filter(article_tit = d)
            final_list = []
            for i in coment_list:
                final_list.append([i, Reply.objects.filter(original_comment = i)])
            return redirect('detailedblog', blog_id = d.id)
        else:
            return redirect('detailedblog', blog_id = d.id)
    else:
        return HttpResponse("<h1>Forbidden</h1>")

    
def reply(request):
    if request.method == 'POST':
        rForm = ReplyForm(request.POST)
        print(request.POST['orig_com'])
        e = get_object_or_404(Comment, pk=request.POST['orig_com'])
        print(request.POST['com_article'])
        d = get_object_or_404(Article, pk=request.POST['com_article'])
        if rForm.is_valid():
            repModel = rForm.save(commit=False)
            repModel.replying_user = request.user
            repModel.original_comment = e
            repModel.save()
            com_form = CommentForm()
            rep_form = ReplyForm()
            likedUserList = d.liked_user.all()
            d1 = Vocab.objects.get(article_title = d)
            s = str(d1.voc)
            w = function_to_render_correct_word_meaning(s)
            w = w[0]
            coment_list = Comment.objects.filter(article_tit = d)
            final_list = []
            for i in coment_list:
                final_list.append([i, Reply.objects.filter(original_comment = i)])
            return redirect('detailedblog', blog_id = d.id)
        else:
            return redirect('detailedblog', blog_id = d.id)
    else:
        return HttpResponse("<h1>Forbidden</h1>")






