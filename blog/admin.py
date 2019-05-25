from django.contrib import admin
from .models import Post
from .models import Page

# Register your models here.

admin.site.register(Page)
admin.site.register(Post)
