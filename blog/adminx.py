#!/usr/bin/env python
# -*- coding:utf-8 -*-


import xadmin
from .models import *


class ArticleAdmin(object):
    style_fields = {'content': 'ueditor'}


xadmin.site.register(Article, ArticleAdmin)
