from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    latest = Post.objects.order_by('-pub_date')[:10]
    output = []
    for item in latest:
        output.append(item.text_public)
    return HttpResponse('\n'.join(output))


def test_view(request):
    groups = Group.objects.all()
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'Test/viewsite.html', {'posts': posts,'groups': groups})


def info(request, username):
    name = User.objects.get(username=username)
    post = Post.objects.filter(author=name)
    # ps = ProfileUser.objects.all()
    return render(request, 'Test/profile.html', {'post': post, 'author': name})


def group(request, title):
    groups = Group.objects.all()
    title_id = Group.objects.get(title=title)
    posts = Post.objects.filter(group=title_id)
    return render(request, 'Test/viewgroup.html', {'posts': posts, 'title': title_id, 'groups': groups})


# def post_id(request, text_public, username):
#     name = User.objects.get(username=username)
#     text = Post.objects.get(text=text_public)
#     return render(request, 'Test/viewpost.html', {'text': text, 'name': name})