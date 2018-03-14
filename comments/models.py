from django.db import models

# Create your models here.
from blog.models import Article


class Comment(models.Model):
    name = models.CharField(verbose_name='用户名', max_length=20)
    email = models.EmailField(verbose_name='用户邮箱')
    text = models.TextField(verbose_name='评论内容')
    created_time = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    article = models.ForeignKey(Article, verbose_name='所属文章')

    class Meta:
        db_table = 't_comments_info'
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text[:20]
