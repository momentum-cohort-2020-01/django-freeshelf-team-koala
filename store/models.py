from django.db import models
from django.utils import timezone

# Create your models here.


class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Author)
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(decimal_places=2, max_digits=8)


class Author(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
