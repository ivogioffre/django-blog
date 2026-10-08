from django.db import models
from django.utils.text import Truncator

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    @property
    def excerpt(self):
        return self.summary or Truncator(self.body).words(30) #si se deja vacio se usan las primeras 30 palabras del texto

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE,
        related_name="comments"
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.author} on '{self.post}'"