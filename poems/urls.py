"""Poems posts view page"""
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('poem_list/', views.PostList.as_view(), name='poem_list'),
    path('<slug:slug>/', views.PoemDetails.as_view(), name='poem_details'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='poem_likes'),
    path('profile', views.Profile, name='profile'),
    path('publish_poem', views.PublishPoem, name='publish_poem'),
]
