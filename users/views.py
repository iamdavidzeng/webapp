from django.shortcuts import render

# Create your views here.
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from .models import *
from .serializers import UserDetailSerializer
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class UserViewset(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """ 用户 """
    serializer_class = UserDetailSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    # def get_serializer_class(self):
    #     pass
    #
    # def get_permissions(self):
    #     pass
    #
    # def create(self, request, *args, **kwargs):
    #     pass
    #
    # def get_object(self):
    #     pass
    #
    # def perform_create(self, serializer):
    #     pass
