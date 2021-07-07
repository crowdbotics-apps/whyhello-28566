from django.conf import settings
from django.db import models


class Jokes(models.Model):
    "Generated Model"
    joke = models.CharField(
        max_length=256,
    )


class Comedians(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
