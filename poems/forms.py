"""Forms file"""
from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    """comment form"""
    class Meta:
        model = Comment
        fields = ('body',)


class PoemForm(forms.ModelForm):
    """Form to publish a poem"""
    class Meta:
        model = Post
        fields = ('title', 'content',)
