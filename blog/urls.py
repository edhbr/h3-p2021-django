from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name='index'),
    path("blog/<slug:slug>", views.single_post, name="blog_post")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
