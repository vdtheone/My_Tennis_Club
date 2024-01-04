from django.db import models
from django.utils import timezone


# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    joined_date = models.DateField(default=timezone.now)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.CharField(max_length=5000)

    def __str__(self):
        return self.name
