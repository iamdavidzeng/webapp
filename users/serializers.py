#!/usr/bin/env python
# -*- coding:utf-8 -*-


from .models import *
from rest_framework import serializers


class UserDetailSerializer(serializers.ModelSerializer):
    """ 用户 """

    class Meta:
        model = UserProfile
        fields = '__all__'


