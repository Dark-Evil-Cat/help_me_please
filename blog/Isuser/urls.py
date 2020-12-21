from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("login/", views.LoginUp.as_view(), name="login"),
    path("exit/", auth_views.auth_logout, name="logout"),
]