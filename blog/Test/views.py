from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import *


def index(request):
    latest = Post.objects.order_by('-pub_date')[:10]
    output = []
    for item in latest:
        output.append(item.text_public)
    return HttpResponse('\n'.join(output))


def test_view(request):
    return render(request, 'base.html', {})