from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model

User = get_user_model()


class Country(models.Model):
    class CountryName(models.TextChoices):
        Germany = "DE"
        France = "FR"
        Poland = "PL"
        Czech_Republic = "CZ"
        United_Kingdom = "UK"
        Italy = "IT"
        Spain = "ES"

    user = models.ForeignKey(User, on_delete=CASCADE)
    country = models.CharField(
        max_length=16, choices=CountryName.choices, null=False, blank=False
    )

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    # TODO: What fields are needed for tax?
    # Every field specific from user
