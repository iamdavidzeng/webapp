#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.test import TestCase
from ..models import *


class ArticleTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Article.objects.create(title='123', author='zzy')

    def test_title(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('title').verbose_name
        self.assertEquals(field_label, '标题')

    def test_author(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('author').verbose_name
        self.assertEquals(field_label, '作者')

    def test_return_str(self):
        article = Article.objects.get(id=1)
        print(article.title)
        field_label = '%s------%s' % (article.title, article.author)
        self.assertEquals(field_label, str(article))

    def test_content(self):
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field('content').max_length
        self.assertEquals(max_length, 9999)
