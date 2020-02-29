from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  
class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
  publish_date = models.DateField(default=timezone.now)
  price = models.DecimalField(decimal_places=2, max_digits=8)
  description = models.TextField()

class Cart(models.Model):
  user = models.ForeignKey(User)
  active = models.BooleanField(default=True)
  order_date = models.DateField(null=True)
  payment_type = models.CharField(max_length=100, null=True)
  payment_id = models.CharField(max_length=100, null=True)

