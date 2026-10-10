from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('posts/', post_list, name='post-list'),
    #path('posts/detail/<pk>', post_detail, name='post-detail'),
]