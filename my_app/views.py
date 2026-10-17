from django.shortcuts import render
from .models import *

def index(request):
    try:
        last_posts = []
        for i in range(3):
            post = Post.published.all().order_by('-publish')[i]
            last_posts.append(post)
    except IndexError:
        last_posts = list(Post.published.all().order_by('-publish'))
    if len(last_posts) == 0:
        return render(request, 'index.html', {'error': "post not find"})
    return render(request, 'index.html', {'last_posts': last_posts})

def post_list(request):
    posts = Post.published.all()
    context = {'posts': posts}
    return render(request, 'post_list.html', context)

