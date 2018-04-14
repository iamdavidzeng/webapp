from django.shortcuts import render
import markdown

# Create your views here.
from .models import *
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import get_object_or_404
from users.models import UserProfile
from comments.forms import CommentForm
from django.db.models import Q
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify

# def index(request):
#     """
#     View function for display all articles.
#     """
#     articles = Article.objects.all()
#     return render(request, 'blog/index.html', context={'articles': articles})


class IndexView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}

        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range

        if page_number == 1:
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True

            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }

        return data


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article'

    def get(self, request, *args, **kwargs):
        response = super(ArticleDetailView, self).get(request, *args, **kwargs)
        return response

    def get_object(self, queryset=None):
        article = super(ArticleDetailView, self).get_object(queryset=None)
        # article.content = markdown.markdown(
        #     article.content,
        #     extensions=[
        #         'markdown.extensions.extra',
        #         'markdown.extensions.codehilite',
        #         'markdown.extensions.toc',
        #     ]
        # )
        # return article
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            TocExtension(slugify=slugify),
        ])
        article.content = md.convert(article.content)
        article.toc = md.toc
        return article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context

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


# def register(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         password = request.POST.get('password')
#         birth = request.POST.get('birth')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         q = UserProfile.objects.filter(first_name=first_name, last_name=last_name)
#         if q:
#             return HttpResponse('此用户名已经被注册')
#         else:
#             q = UserProfile(first_name=first_name, last_name=last_name,
#                             birth=birth, phone=phone, email=email, password=password)
#             q.save()
#             return HttpResponse('用户注册成功')
#     return render(request, 'blog/register.html')
#
#
# def login(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         password = request.POST.get('password')
#         q = UserProfile.objects.filter(first_name=first_name, last_name=last_name, password=password)
#         if q:
#             return HttpResponse('登陆成功')
#         else:
#             return HttpResponse('登陆失败,用户名或密码错误')
#     return render(request, 'blog/login.html')


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'blog/index.html', {'error_msg': error_msg})

    articles = Article.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    return render(request, 'blog/index.html', {'error_msg': error_msg, 'articles': articles})
