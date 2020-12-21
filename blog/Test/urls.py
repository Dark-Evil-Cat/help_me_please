from django.urls import path
from . import views


urlpatterns = [
    path("", views.test_view, name="test_view"),
    path("ex", views.index, name="index"),
    path("user/<str:username>/", views.info, name="info"),
    path("group/<str:title>/", views.group, name="group"),
    # path("registration", views.registration, name="registration"),
    # path("post/<str:username>/", views.post_id, name="post_id"),
]