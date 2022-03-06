from django.db import models
from django.utils import timezone
from user.models import *
from .managers import PostsManager


class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    pic = models.ImageField(verbose_name="post", null=True, upload_to='images/')
    description = models.TextField(max_length=255, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    objects = PostsManager()

    def __str__(self):
        return f"{self.username}, {self.title}"


class Comments(models.Model):
    username = models.ForeignKey(User, related_name='username', on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, related_name='post_comment', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    comment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.username, self.post)
