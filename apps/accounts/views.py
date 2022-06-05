from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import login, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.views import (
    LogoutView,
    LoginView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from django.views.generic import UpdateView, View
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)
from .forms import SignupForm, ProfileForm
from .token import account_activation_token

User = get_user_model()


class SignUp(View):
    form_class = SignupForm
    template_name = "accounts/register.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save()

            current_site = get_current_site(request)
            subject = "Activate Your Account"
            use_https = self.request.is_secure()
            message = render_to_string(
                "accounts/account_activation_email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                    "protocol": "https" if use_https else "http",
                },
            )
            user.email_user(subject, message)
            messages.success(
                request, ("Please Confirm your email to complete registration.")
            )
            return redirect("index")
        return render(request, self.template_name, {"form": form})


class ActivateAccount(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            messages.success(request, ("Your account have been confirmed."))
            return redirect("index")
        else:
            messages.warning(
                request,
                (
                    "The confirmation link was invalid, possibly because it has already been used."
                ),
            )
            return redirect("index")


class LogIn(LoginView):
    form_class = AuthenticationForm
    template_name = "accounts/login.html"

    def get_success_url(self):
        """Automatically redirect depends on user status."""
        if self.request.user.is_superuser:
            return reverse("admin:index")
        else:
            return reverse("index")


class LogOut(LogoutView):
    template_name = "accounts/logout.html"


class Profile(UpdateView):
    context_object_name = "variable_used_in `profile.html`"
    form_class = ProfileForm
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
