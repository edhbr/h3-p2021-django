from django.db import models
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    published_date = models.DateField("date published")
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    featured_image = models.ImageField()
    lead = models.TextField()
    body = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return "({}) - {}".format(self.published_date, self.title)


class Page(models.Model):
    path = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    punchline = models.CharField(max_length=200)
    featured_post = models.ForeignKey(
        Post, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "({}) - {}".format(self.path, self.title)
