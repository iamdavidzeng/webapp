from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()


class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=20)
    author = models.CharField(verbose_name='作者', max_length=20, blank=True, null=True)
    ctime = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    content = models.CharField(verbose_name='文章内容', max_length=9999, blank=True, null=True)
    memo = models.CharField(verbose_name='备注', max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_blog_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title + '------' + self.author
