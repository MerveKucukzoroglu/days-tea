"""Forms file"""
from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """comment form"""
    class Meta:
        model = Comment
        fields = ('body',)
