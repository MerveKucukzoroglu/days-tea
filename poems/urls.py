"""Poems posts view page"""
from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PoemDetails.as_view(), name='poem_details'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='poem_likes'),
]
