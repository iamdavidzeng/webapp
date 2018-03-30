from django.urls import reverse
from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from DjangoUeditor.models import UEditorField

User = get_user_model()


class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=20)
    author = models.CharField(verbose_name='作者', max_length=20, blank=True, null=True)
    ctime = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    content = UEditorField(verbose_name='内容', width=600, height=300, toolbars='full',
                           imagePath='images/', filePath='', upload_settings={'imageMaxSize': 1204000,
                            'videoPathFormat': "videos/%(basename)s_%(datetime)s.%(extname)s"}, default='')
    memo = models.CharField(verbose_name='备注', max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_blog_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:detail', args=[str(self.id)])

    def __str__(self):
        return self.title + '------' + self.author
