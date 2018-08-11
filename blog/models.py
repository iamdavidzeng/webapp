import markdown
from django.urls import reverse
from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.utils.html import strip_tags

User = get_user_model()


class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=20)
    author = models.CharField(verbose_name='作者', max_length=20, blank=True, null=True)
    content = models.TextField(verbose_name='文章内容', blank=True, null=True)
    memo = models.CharField(verbose_name='备注', max_length=255, blank=True, null=True)
    views = models.PositiveIntegerField(verbose_name='阅读量', default=0)
    excerpt = models.CharField(verbose_name='文章摘要', max_length=200, blank=True, null=True)
    ctime = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)

    class Meta:
        db_table = 't_blog_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:detail', args=[str(self.id)])

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.content))[:66]
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title + '------' + self.author
