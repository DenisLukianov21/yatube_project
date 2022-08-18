from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Post(models.Model):
    group = models.ForeignKey('Group',
                              blank=True,
                              null=True,
                              on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='post'
    )


class Group(models.Model):
    title = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.slug
