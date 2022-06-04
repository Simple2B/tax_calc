from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

from apps.transactions.models import Transaction

User = get_user_model()


@login_required
def vat_return(request):
    ...


@login_required
def summary(request):
    ...


@login_required
def ecsl(request):
    ...


@login_required
def statistical_survey(request):
    ...


@login_required
def sales_vat(request):
    ...


@login_required
def fc_ics(request):
    ...


@login_required
def fc_ics_piv(request):
    ...


@login_required
def ics(request):
    ...


@login_required
def ics_piv(request):
    ...


@login_required
def fc_ica(request):
    ...


@login_required
def fc_ica_pivot(request):
    ...


@login_required
def import_vat(request):
    ...


@login_required
def export(request):
    ...


@login_required
def transfer(request):
    page_number = request.GET.get("page")
    activity_period = request.GET.get("activity_period")
    transactions = Transaction.objects.filter(user=request.user)
    paginator = Paginator(transactions, 50)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "count": len(transactions),
        "headers": [field.name.upper() for field in Transaction._meta.get_fields()][2:],
        "data": page_obj,
    }
    return render(request, "taxes/transfer.html", context)
