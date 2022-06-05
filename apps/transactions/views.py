import io, csv
from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
)
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Count
import pandas as pd
from .models import Transaction
from config.settings import PAGINATE_BY
from apps.countries.models import Country
from .forms import UploadFileForm

User = get_user_model()


@login_required
def transactions(request):
    transactions = Transaction.objects.filter(user=request.user)
    paginator = Paginator(transactions, PAGINATE_BY)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    context = {
        "count": len(transactions),
        "headers": [
            "UNIQUE_ACCOUNT_IDENTIFIER",
            "ACTIVITY_PERIOD",
            "SALES_CHANNEL",
            "MARKETPLACE",
        ],
        "data": page,
    }
    return render(request, "transaction/list.html", context)


class TransactionDetail(LoginRequiredMixin, DetailView):
    model = Transaction


class TransactionsUpload(LoginRequiredMixin, View):
    form_class = UploadFileForm
    template_name = "transaction/upload.html"
    success_url = "transaction/transactions.html"

    def get_context(self, request, *args, **kwargs):
        statistics = (
            Transaction.objects.filter(user=request.user)
            .values("activity_period")
            .annotate(transaction_count=Count("id"))
        )
        context = {
            "headers": [
                "ACTIVITY PERIOD",
                "SIZE",
            ],
            "data": statistics,
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context(request)
        context["form"] = self.form_class()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(request)
        context["form"] = self.form_class(request.POST, request.FILES)
        if context["form"].is_valid():
            file = request.FILES["file"]
            if not file.name.endswith(".csv"):
                messages.warning(request, "File is not CSV type")
                return redirect("transactions:upload")
            df = pd.read_csv(
                request.FILES["file"],
                dtype=object,
            ).fillna(0)

            for index, row in df.iterrows():
                obj = {k.lower(): v for k, v in row.to_dict().items()}
                obj["user"] = User.objects.get(id=request.user.id)
                obj["activity_period"] = pd.to_datetime(
                    obj.get("activity_period")
                ).date()
                obj["tax_calculation_date"] = pd.to_datetime(
                    obj.get("tax_calculation_date")
                ).date()
                obj["transaction_depart_date"] = pd.to_datetime(
                    obj.get("transaction_depart_date")
                ).date()
                obj["transaction_arrival_date"] = pd.to_datetime(
                    obj.get("transaction_arrival_date")
                ).date()
                obj["transaction_complete_date"] = pd.to_datetime(
                    obj.get("transaction_complete_date")
                ).date()
                obj["vat_inv_exchange_rate_date"] = pd.to_datetime(
                    obj.get("vat_inv_exchange_rate_date")
                ).date()
                try:
                    transaction = Transaction(**obj)
                    transaction.save()
                    transaction.full_clean()
                except:
                    messages.warning(
                        request, ("Failed in transaction".format(transaction))
                    )
            messages.success(request, ("File posted successfully"))
            return render(request, self.success_url)
        else:
            messages.warning(request, ("Failed to upload file"))
        return render(request, self.template_name, context)


class TransactionUpdate(LoginRequiredMixin, UpdateView):
    model = Transaction
