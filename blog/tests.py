#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.test import TestCase, Client
from .views import *
from django.urls import reverse

# Create your tests here.


class ArticleTest(TestCase):

    def test_my_blog_list(self):
        response = self.client.get(reverse('blog:all_blog'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, )

    def test_hello(self):
        response = self.client.get(reverse('blog:hello'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'hello world!')
