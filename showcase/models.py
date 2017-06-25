from django.db import models

from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    icon = models.ImageField()
    image = models.ImageField()
    tags = models.ManyToManyField(Tag, blank=True)
    description = models.CharField(max_length=300)
    stock = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    visible = models.BooleanField(default=True)
    sold = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
