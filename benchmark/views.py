from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.utils.translation import ugettext as _

from .forms import CRITERIA_BLUE, CRITERIA_RED, CustomerBlueForm, CustomerRedForm


def is_member_staff(user):
    return user.groups.filter(name='staff').exists()

def is_member_customers(user):
    return user.groups.filter(name__in=['staff', 'customers']).exists()


@login_required
@user_passes_test(is_member_staff)
def staff_blue(request):
    return render(request, 'benchmark/staff.html', {
        "team": "blue"
    })


@login_required
@user_passes_test(is_member_staff)
def staff_red(request):
    return render(request, 'benchmark/staff.html', {
        "team": "red"
    })


@login_required
@user_passes_test(is_member_customers)
def customer_blue(request):
    form = CustomerBlueForm()
    return render(request, 'benchmark/customer.html', {
        "team": "blue",
        "form": form
    })


@login_required
@user_passes_test(is_member_customers)
def customer_red(request):
    form = CustomerRedForm()
    return render(request, 'benchmark/customer.html', {
        "team": "red",
        "form": form
    })


@login_required
@user_passes_test(is_member_customers)
def benchmark_blue(request):
    if request.method == 'POST':
        form = CustomerBlueForm(data=request.POST)
        criteria = {}
        if form.is_valid():
            for criterion in form.cleaned_data.items():
                name, weight = criterion
                criteria[name] = weight
            # generate PDF document
            # return PDF document
            return HttpResponse(1337)
        else:
            messages.error(request, _('Formulaire invalide.'))
    else:
        return redirect(reverse('customer_blue'))
    pass


@login_required
@user_passes_test(is_member_customers)
def benchmark_red(request):
    pass