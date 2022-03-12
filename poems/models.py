"""Database Model for Poems App"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """Poems Model"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="poem_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='poem_likes', blank=True)

    class Meta:
        """created on field"""
        ordering = ['-created_on']

    def __str__(self):
        """return self title"""
        return self.title

    def number_of_likes(self):
        """number of likes in a post"""
        return self.likes.count()


class Comment(models.Model):
    """Comments model class"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """meta class for comments"""
        ordering = ['created_on']

    def __str__(self):
        """comment str return"""
        return f"Comment {self.body} by {self.name}"
