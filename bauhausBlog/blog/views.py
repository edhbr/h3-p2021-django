from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.conf import settings

from .models import Post, Page


def index(request):
    home = Page.objects.get(path="/")
    blog_posts = Post.objects.order_by("-published_date")

    home.featured_post.featured_image = settings.MEDIA_URL + \
        str(home.featured_post.featured_image)

    for post in blog_posts:
        post.featured_image = settings.MEDIA_URL + str(post.featured_image)

    home.blog_posts = blog_posts
    return render(request, "pages/index.html", {"data": home})


def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    post.featured_image = settings.MEDIA_URL + str(post.featured_image)

    return render(request, "posts/single.html", {"data": post})
