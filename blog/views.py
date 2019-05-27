from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.conf import settings

from .models import Post, Page


def index(request):
    home = get_object_or_404(Page, path="/")
    blog_posts = Post.objects.order_by("-published_date")

    home.blog_posts = blog_posts
    return render(request, "pages/index.html", {"data": home})


def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, "posts/single.html", {"data": post})
