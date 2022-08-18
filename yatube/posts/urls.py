# posts/urls.py
from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='best_index'),
    path('group/<slug:slug>/', views.group_posts, name='group')
]
