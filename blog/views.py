from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import HttpResponse
from django.views import generic
from django.http import Http404
from django.shortcuts import get_object_or_404


# def index(request):
#     """
#     View function for display all articles.
#     """
#     articles = Article.objects.all()
#     return render(request, 'blog/index.html', context={'articles': articles})


class IndexView(generic.ListView):
    template_name = 'blog/index.html'

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
