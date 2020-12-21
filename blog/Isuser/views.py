from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CreationForm, AuthUserLogin
from django.shortcuts import render


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("signup")
    template_name = "Isuser/signup.html"


class LoginUp(LoginView):
    form_class = AuthUserLogin
    success_url = reverse_lazy("login")
    template_name = "Isuser/registration/login.html"


# class ExitUp(LogoutView):
#     form_class = ExitUser
#     success_url = reverse_lazy("logger_out")
#     template_name = "Isuser/registration/logged_out.html"
