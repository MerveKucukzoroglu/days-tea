"""Views file for the Poems"""
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    """Site pagination and order of poems"""
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PoemDetails(View):
    """Open and view a post"""
    def get(self, request, slug, *args, **kwargs):
        """getting relevent post information"""
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "poem_details.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
