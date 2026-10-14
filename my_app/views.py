from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post-list.html', {'posts': posts})

