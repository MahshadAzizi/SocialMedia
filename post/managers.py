from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone


class PostsManager(models.Manager):
    def get_query_set(self):
        return super().get_queryset().filter(date_posted__gte=datetime.now() - timedelta(days=7))


