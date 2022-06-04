from django.contrib.auth.views import (
    LogoutView,
    LoginView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/register.html"


class LogIn(LoginView):
    form_class = AuthenticationForm
    template_name = "accounts/login.html"

    def get_success_url(self):
        """Automatically redirect depens on user status."""
        if self.request.user.is_superuser:
            return reverse("admin:index")
        else:
            return reverse("index")


class LogOut(LogoutView):
    template_name = "accounts/logout.html"


class Profile(UpdateView):
    context_object_name = "variable_used_in `profile.html`"
    form_class = UserChangeForm
    success_url = reverse_lazy("index")
    template_name = "accounts/profile.html"

    def get_object(self, queryset=None):
        return self.request.user


class ResetPassword(PasswordResetView):
    form_class = PasswordResetForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/password_reset_form.html"
    email_template_name = "accounts/password_reset_email.html"
    subject_template_name = "accounts/password_reset_subject.txt"


class ResetPasswordConfirm(PasswordResetConfirmView):
    form_class = SetPasswordForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/password_reset_confirm.html"
