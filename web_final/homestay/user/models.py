from django.db import models
from django.contrib import messages
from django.core import validators
from django.core.validators import *


class Room(models.Model):
    name = models.CharField(max_length=250, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField(max_length=20000, null=True)

    def __str__(self):
        return self.name

    @property
    def image_URL(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url
