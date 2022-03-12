"""Poems posts view page"""
from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
]
