from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, blank=True)
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField()
    reviews = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User, related_name="favorites", on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, related_name="favorites", on_delete=models.CASCADE)

    def __str__(self):
        return f'Favorite: {self.user, self.book}'

# class Image(models.Model):
#     image_name = models.CharField(max_length=400)
#     imagefile = models.FileField(
#         upload_to='images', null=True, verbose_name=None)

#     def __str__(self):
#         return f'{self.name} {self.imagefile}'
#         return f"Book: {self.title} description: {self.description}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=True)
    order_date = models.DateField(null=True)
    payment_type = models.CharField(max_length=100, null=True)
    payment_id = models.CharField(max_length=100, null=True)
