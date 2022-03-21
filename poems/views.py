"""Views file for the Poems"""
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PoemForm
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


class PostList(generic.ListView):
    """Site pagination and order of poems"""
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'poem_list.html'
    paginate_by = 6


def profile(request):
    """Site pagination and order of poems"""
    return render(request, 'profile.html')


def publish(request):
    """publish poem as authenticated user"""
    if request.method == 'POST':
        poem_form = PoemForm(request.POST, request.FILES)

        if poem_form.is_valid():
            form = poem_form.save(commit=False)
            form.author = User.objects.get(username=request.user.username)
            form.slug = form.title.replace(" ", "-")
            messages.success(
                request, 'Your poem is successfully submitted for approval'
                )
            form.save()
        return redirect('my_poems')

    poem_form = PoemForm()
    context = {'poem_form': poem_form}

    return render(
        request,
        'publish.html', context
    )


def myPoems(request):
    logged_in_user = request.user
    logged_in_user_posts = Post.objects.filter(author=logged_in_user)
    return render(request, 'my_poems.html', {'posts': logged_in_user_posts})


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
                "liked": liked,
                "commented": False,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """posting comments"""
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "poem_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    """class view for like and unlike a post"""
    def post(self, request, slug):
        """function to like/unlike"""
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('poem_details', args=[slug]))
