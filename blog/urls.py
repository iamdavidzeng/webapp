#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^all/', my_blog_list, name='all_blog'),
    url(r'^hello/', hello, name='hello'),

]