from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .forms import RegisterForm,LoginForm
from django.contrib.auth.views import LoginView
# Create your views here.
#login
#logout
#register
#create_Poll

class  SignupView(CreateView):
    template_name = "userprofile/signup.html"
    form_class = RegisterForm
    success_url = "signin"


class SigninView(LoginView):
    template_name = "userprofile/signin.html"

    success_url =  reverse_lazy("/")