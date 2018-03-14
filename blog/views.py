from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import HttpResponse
from django.views import generic
from django.http import Http404
from django.shortcuts import get_object_or_404
from users.models import UserProfile


# def index(request):
#     """
#     View function for display all articles.
#     """
#     articles = Article.objects.all()
#     return render(request, 'blog/index.html', context={'articles': articles})


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all()


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'blog/article.html'

    # def article_detail_view(request, id):
    #     # try:
    #     #     article_id = Article.objects.get(pk=pk)
    #     # except Article.DoesNotExist:
    #     #     raise Http404('Book does not exsit')
    #     article = get_object_or_404(Article, id=id)
    #
    #     return render(
    #         request,
    #         'blog/article.html',
    #         context={'article': article}
    #     )
# def detail(request, id):
#     article = get_object_or_404(Article, id=id)
#     return render(request, 'blog/article.html', {'article': article})


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        birth = request.POST.get('birth')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        q = UserProfile.objects.filter(first_name=first_name, last_name=last_name)
        if q:
            return HttpResponse('此用户名已经被注册')
        else:
            q = UserProfile(first_name=first_name, last_name=last_name,
                            birth=birth, phone=phone, email=email)
            q.save()
            return HttpResponse('用户注册成功')
    return render(request, 'blog/register.html')


def login(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        q = UserProfile.objects.filter(first_name=first_name, last_name=last_name, password=password)
        if q:
            return HttpResponse('登陆成功')
        else:
            return HttpResponse('登陆失败,用户名或密码错误')
    return render(request, 'blog/login.html')
