#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<pk>\d+)/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login, name='login'),
    url(r'^search', views.search, name='search'),


]
