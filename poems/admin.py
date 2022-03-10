"""admin panel"""
from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """summernote model for admin"""
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('approved', 'created_on')
    summernote_fields = ('content')
