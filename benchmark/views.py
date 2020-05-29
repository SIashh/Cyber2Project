from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.utils.translation import ugettext as _

from .forms import CRITERIA_BLUE, CRITERIA_RED, CustomerBlueForm, CustomerRedForm, StaffBlueForm


def is_member_staff(user):
    return user.groups.filter(name='staff').exists()

def is_member_customers(user):
    return user.groups.filter(name__in=['staff', 'customers']).exists()


@login_required
@user_passes_test(is_member_staff)
def staff_blue(request):
    form1 = StaffBlueForm()
    form2 = StaffBlueForm()
    return render(request, 'benchmark/staff.html', {
        "team": "défensives",
        "form1" : form1,
        "form2" : form2
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
        form = StaffBlueForm(data=request.POST)
        form2 = StaffBlueForm(data=request.POST)

        criteria = {}

        if form2.is_valid():
            for criterion in form2.cleaned_data.items():
                print(criterion)
                name, weight = criterion
                criteria[name] = weight
        if form.is_valid():
            for criterion in form.cleaned_data.items():
                print(criterion)
                name, weight = criterion
                criteria[name] = weight
                first_tool = "Nessus" #Exemples, à modifier
                second_tool = "Qualys" #Exemples, à modifier
            # generate PDF document
            # return PDF document
            return render(request, 'benchmark/report.html', {
                "team": "blue",
                "first_tool": first_tool,
                "second_tool": second_tool
            })
        else:
            messages.error(request, _('Formulaire invalide.'))
    else:
        return redirect(reverse('customer_blue'))
    pass

@login_required
@user_passes_test(is_member_customers)
def benchmark_red(request):
    pass