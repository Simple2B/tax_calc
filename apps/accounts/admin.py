from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import SignupForm, ProfileForm
from .models import User


@admin.register(User)
class Admin(UserAdmin):
    add_form = SignupForm
    form = ProfileForm
    model = User
    list_display = (
        "username",
        "email",
        "last_login",
        "date_joined",
        "is_staff",
        "is_active",
        "is_superuser",
    )
    list_filter = (
        "last_login",
        "date_joined",
        "is_superuser",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_superuser", "is_staff", "is_active")}),
        (
            "Group Permissions",
            {
                "classes": ("collapse",),
                "fields": (
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            "Personal info",
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name"),
            },
        ),
        (
            "Permissions",
            {
                "classes": ("wide",),
                "fields": ("is_superuser", "is_staff", "is_active"),
            },
        ),
        (
            "Group Permissions",
            {
                "classes": ("collapse",),
                "fields": (
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("username", "email")
    readonly_fields = ("date_joined", "last_login")
    ordering = ("email",)
