"""admin panel"""
from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """summernote model for admin"""
    list_display = ('title', 'slug', 'approved', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('approved', 'created_on')
    summernote_fields = ('content',)
    actions = ['approve_poems']

    def approve_poems(self, request, queryset):
        """approve poems function"""
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment admin panel"""
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('name', 'created_on')
    search_fields = ('name', 'email', 'body')
