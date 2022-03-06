from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=12, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=50, null=True, blank=True, unique=True)
    national_number = models.CharField(max_length=20, null=True, blank=True, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
