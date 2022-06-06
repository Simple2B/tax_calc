from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    """
    Class implementing a fully featured User model with
    admin-compliant permissions.

    Username, email and password are required. Other fields are optional.
    """

    email = models.EmailField(
        _("email address"),
        max_length=254,
        unique=True,
        help_text=_(
            "Required. 254 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_("Designates whether this user should be treated as active. "),
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = "auth"
        verbose_name = "user"
        verbose_name_plural = "users"
