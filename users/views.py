from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from .models import *
from .serializers import UserDetailSerializer
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth import get_user_model
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse
from django.contrib import auth
from django.http import HttpResponsePermanentRedirect
User = get_user_model()


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


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            if user is not None:
                user = auth.authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
                auth.login(request, user)
                return redirect('/')
        auth.logout(request)
        return render(request, 'users/register.html', {'errors': form.errors})
    else:
        context = {
            'form': RegisterForm()
        }
    return render(request, 'users/register.html')


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                auth.login(request, user)
                return redirect('/')
        auth.logout(request)
        print(form.errors)
        return render(request, 'users/login.html', {'errors': form.errors})
    else:
        context = {
            'form': LoginForm(),
        }
    return render(request, 'users/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def password(request):
    pass


def updateImage(request):
    pass
