from django.conf import settings
from django.db import models


class Jokes(models.Model):
    "Generated Model"
    joke = models.CharField(
        max_length=256,
    )
    comedian = models.OneToOneField(
        "home.Comedians",
        on_delete=models.PROTECT,
        related_name="jokes_comedian",
    )


class Comedians(models.Model):
    "Generated Model"
    cname = models.OneToOneField(
        "home.Jokes",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="comedians_cname",
    )
