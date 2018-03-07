from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import HttpResponse


def my_blog_list(request):
    blog_list = Article.objects.all()
    return render(request, 'blog/show_article.html', {'blog_list': blog_list})


def hello(request):
    return HttpResponse('hello world!')
