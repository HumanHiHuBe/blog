from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Article, CategoryClass, Vocab
from .forms import ArticleForm, VocabForm
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
    return render(request, 'blogapp/signupuser.html')

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
        return HttpResponse("<h1>Forbidden</h1>")
    else:
        d = get_object_or_404(Article, pk=blog_id)
        d1 = Vocab.objects.get(article_title = d)
        s = str(d1.voc)
        w = function_to_render_correct_word_meaning(s)
        w = w[0]
        # try:
        #     w = function_to_render_correct_word_meaning(s)
        # except:
        #     return render(request, 'blogapp/detailedblog.html', {'article':d, 'msg':'Format of your Vocab is not correct.'})
        return render(request, 'blogapp/detailedblog.html', {'article':d, 'words': w})

#view for like habdling
def likescount(request):
    if request.POST:
        d = get_object_or_404(Article, pk=request.POST['article_id'])
        d.likes = d.likes + 1
        d.save()
        d = get_object_or_404(Article, pk=request.POST['article_id'])
        d1 = Vocab.objects.get(article_title = d)
        s = str(d1.voc)
        w = function_to_render_correct_word_meaning(s)
        w = w[0]
        return render(request, 'blogapp/detailedblog.html', {'article':d, 'words': w})
    else:
        return HttpResponse("<h1>Forbidden</h1>")



#View for Detailed Vocab
def individualvocab(request, vocab):
    q = word_dictionary(vocab)
    if int(q[0].status_code) == 200:
        d = {'word':vocab, 'code':int(q[0].status_code)}
        v=q[1]
        try:
            d['cat'] = v['results'][0]['lexicalEntries'][0]['lexicalCategory']['text']
        except:
            pass
        try:
            d['def'] = v['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        except:
            pass
        try:
            d['pro'] = v['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][1]['audioFile']
        except:
            pass
        try:
            d['ex1'] = v['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['text']
        except:
            pass
                
        return render(request, 'blogapp/individualvocab.html', d)
    else:
        return render(request, 'blogapp/individualvocab.html', {'word':vocab, 'code':int(q[0].status_code) , 'msg':'Maybe Some Error Occured, Please Retry Only Once If Did Not Work Then Maybe There Is No More Detail Available For Your Searched Word, - {}.'.format(vocab)})


#View for writing blog
@login_required
def writeblog(request):
    if request.POST:
        form1 = ArticleForm(request.POST)
        if form1.is_valid():
            model1 = form1.save(commit= False)
            # model1.save()
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
        return render(request, 'blogapp/writeblog.html', {'form1': ArticleForm(), 'form2':VocabForm(), 'msg': 'Saved Sucessfully', 'model1': model1})
    else:
        return render(request, 'blogapp/writeblog.html', {'form1': ArticleForm(), 'form2':VocabForm(), 'msg':''})

# def bloghome(request):
#     if request.method == 'POST':
#         f = dum(request.POST, request.FILES)
#         if f.is_valid():
#             f.save()
#         else:
#             return render(request, 'blogapp\home.html', {'form' : dum(),'afterform':f.errors, 'uploaded':''})
#         try:          
#             return render(request, 'blogapp\home.html', {'form' : dum(),'afterform':'You have uploaded following items', 'uploaded': fi.objects.get(title = request.POST['title'])})
#         except:
#             return render(request, 'blogapp\home.html', {'form' : dum(),'afterform':'You have uploaded following items', 'uploaded': ''})
#     else:
#         return render(request, 'blogapp\home.html', {'form' : dum(),'afterform':'', 'uploaded':''})






