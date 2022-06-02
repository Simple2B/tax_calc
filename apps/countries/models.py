from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model

User = get_user_model()


class Countries(models.Model):
    class Country(models.TextChoices):
        DE = "Germany"
        FR = "France"
        PL = "Poland"
        CZ = "Czech Republic"
        UK = "United Kingdom"
        IT = "Italy"
        ES = "Spain"

    user = models.ForeignKey(User, on_delete=CASCADE)
    country = models.CharField(
        max_length=16, choices=Country.choices, null=False, blank=False
    )
    # TODO: What fields are needed for tax?
    # Every field specific from user
