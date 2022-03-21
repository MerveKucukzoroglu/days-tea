"""Poems posts view page"""
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('poem_list/', views.PostList.as_view(), name='poem_list'),
    path('<slug:slug>/', views.PoemDetails.as_view(), name='poem_details'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='poem_likes'),
    path('profile', views.profile, name='profile'),
    path('publish', views.publish, name='publish'),
    path('my_poems', views.myPoems, name='my_poems'),
    path('pending_approval', views.pendingApproval, name='pending_approval'),
]
