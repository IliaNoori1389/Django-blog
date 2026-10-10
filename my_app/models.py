from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class DraftManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="draft")

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")

class Post(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = 'draft'
        PUBLISHED = 'published'

    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=250)
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=StatusChoices, default=StatusChoices.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    objects = models.Manager()
    published = PublishedManager()
    draft = DraftManager()
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]


