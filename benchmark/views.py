from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.utils.translation import ugettext as _

from .models import BlueNote, BlueWeight, RedNote, RedWeight, Tool

from .forms import (
    CRITERIA_BLUE,
    CRITERIA_RED,
    CustomerBlueForm,
    CustomerRedForm,
    StaffBlueForm,
    StaffRedForm,
)


def is_member_staff(user):
    return user.groups.filter(name="staff").exists()


def is_member_customers(user):
    return user.groups.filter(name__in=["staff", "customers"]).exists()


def staff_valid_data(team, form):
    # DB data
    customers = [u.id for u in User.objects.filter(groups__name="customers")]
    tools = [t.id for t in Tool.objects.all()]
    if team == "blue":
        notes = [
            (rn.customer_id, rn.tool_id) for rn in BlueNote.objects.all()
        ]  # (customer, tool)
    elif team == "red":
        notes = [
            (rn.customer_id, rn.tool_id) for rn in RedNote.objects.all()
        ]  # (customer, tool)

    # Form data
    customer = int(form.cleaned_data.get("customer"))
    tool = int(form.cleaned_data.get("tool"))

    # Check that customer and tool exist
    if customer not in customers or tool not in tools:
        return False

    # Check that the tool has not been already noted
    if (customer, tool) in notes:
        return False

    return True


def customer_valid_data(request):
    customers = [u.id for u in User.objects.filter(groups__name="customers")]
    customer = request.user.id
    if customer not in customers:
        return False
    return True


@login_required
@user_passes_test(is_member_staff)
def staff_blue(request):
    if request.method == "POST":
        form = StaffBlueForm(request.POST)
        if form.is_valid():
            # Further verification
            if staff_valid_data("blue", form):
                note = BlueNote(
                    customer_id=form.cleaned_data.get("customer"),
                    tool_id=form.cleaned_data.get("tool"),
                    detection=form.cleaned_data.get("detection"),
                    capacite_d_analyse=form.cleaned_data.get(
                        "capacite_d_analyse"
                    ),
                    complexite_d_analyse=form.cleaned_data.get(
                        "complexite_d_analyse"
                    ),
                    export_des_resultats=form.cleaned_data.get(
                        "export_des_resultats"
                    ),
                    creation_de_regles=form.cleaned_data.get(
                        "creation_de_regles"
                    ),
                    export_de_fichier_suspect=form.cleaned_data.get(
                        "export_de_fichier_suspect"
                    ),
                    prevention=form.cleaned_data.get("prevention"),
                )
                note.save()
                messages.success(request, _("Notation enregistrée !"))
                return redirect(reverse("staff_blue"))
            else:
                messages.error(request, _("Données invalides."))
                return redirect(reverse("staff_blue"))
        else:
            messages.error(request, _("Formulaire invalide."))
            return redirect(reverse("staff_blue"))
    else:
        form = StaffBlueForm()
        return render(
            request, "benchmark/staff.html", {"team": "blue", "form": form}
        )


@login_required
@user_passes_test(is_member_staff)
def staff_red(request):
    if request.method == "POST":
        form = StaffRedForm(request.POST)
        if form.is_valid():
            # Further verification
            if staff_valid_data("red", form):
                note = RedNote(
                    customer_id=form.cleaned_data.get("customer"),
                    tool_id=form.cleaned_data.get("tool"),
                    mise_a_jour=form.cleaned_data.get("mise_a_jour"),
                    capacite_de_detection=form.cleaned_data.get(
                        "capacite_de_detection"
                    ),
                    configuration=form.cleaned_data.get("configuration"),
                    rapidite_d_execution=form.cleaned_data.get(
                        "rapidite_d_execution"
                    ),
                    comsommation_de_ressources=form.cleaned_data.get(
                        "comsommation_de_ressources"
                    ),
                    explication_de_vulnerabilite=form.cleaned_data.get(
                        "explication_de_vulnerabilite"
                    ),
                    documentation=form.cleaned_data.get("documentation"),
                    scope_de_scan=form.cleaned_data.get("scope_de_scan"),
                    flexibilite=form.cleaned_data.get("flexibilite"),
                    communaute=form.cleaned_data.get("communaute"),
                    compatibilite_avec_outis_externes=form.cleaned_data.get(
                        "compatibilite_avec_outis_externes"
                    ),
                )
                note.save()
                messages.success(request, _("Notation enregistrée !"))
                return redirect(reverse("staff_red"))
            else:
                messages.error(request, _("Données invalides."))
                return redirect(reverse("staff_red"))
        else:
            messages.error(request, _("Formulaire invalide."))
            return redirect(reverse("staff_red"))
    else:
        form = StaffRedForm()
        return render(
            request, "benchmark/staff.html", {"team": "red", "form": form}
        )


@login_required
@user_passes_test(is_member_customers)
def customer_blue(request):
    if request.method == "POST":
        form = CustomerBlueForm(data=request.POST)
        if form.is_valid():
            # Is there already an entry in DB?
            customers_blueweights = [bn.customer_id for bn in BlueWeight.objects.all()]
            customer = request.user.id
            if customer not in customers_blueweights:
                # No, Insert in DB
                weight = BlueWeight(
                    customer_id=customer,
                    detection=form.cleaned_data.get('detection'),
                    capacite_d_analyse=form.cleaned_data.get('capacite_d_analyse'),
                    complexite_d_analyse=form.cleaned_data.get('complexite_d_analyse'),
                    export_des_resultats=form.cleaned_data.get('export_des_resultats'),
                    creation_de_regles=form.cleaned_data.get('creation_de_regles'),
                    export_de_fichier_suspect=form.cleaned_data.get('export_de_fichier_suspect'),
                    prevention=form.cleaned_data.get('prevention')
                )
                print()
                print()
                print(weight.detection)
                print()
                print()
                weight.save()
                messages.success(request, _("Pondération enregistrée !"))
                return redirect(reverse("customer_blue"))
            else:
                # Yes, update in DB
                weight = BlueWeight.objects.get(customer_id=customer)
                weight.detection=int(form.cleaned_data.get('detection')),
                weight.capacite_d_analyse=int(form.cleaned_data.get('capacite_d_analyse')),
                weight.complexite_d_analyse=int(form.cleaned_data.get('complexite_d_analyse')),
                weight.export_des_resultats=int(form.cleaned_data.get('export_des_resultats')),
                weight.creation_de_regles=int(form.cleaned_data.get('creation_de_regles')),
                weight.export_de_fichier_suspect=int(form.cleaned_data.get('export_de_fichier_suspect')),
                weight.prevention=int(form.cleaned_data.get('prevention'))
                weight.save()
                messages.success(request, _("Pondération mise à jour !"))
                return redirect(reverse("customer_blue"))
        else:
            messages.error(request, _("Formulaire invalide."))
            return redirect(reverse("customer_blue"))
    else:
        form = CustomerBlueForm()
        return render(
            request, "benchmark/customer.html", {"team": "blue", "form": form}
        )


@login_required
@user_passes_test(is_member_customers)
def customer_red(request):
    form = CustomerRedForm()
    return render(
        request, "benchmark/customer.html", {"team": "red", "form": form}
    )


@login_required
@user_passes_test(is_member_customers)
def benchmark_blue(request):
    if request.method == "POST":
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
                first_tool = "Nessus"  # Exemples, à modifier
                second_tool = "Qualys"  # Exemples, à modifier
            # generate PDF document
            # return PDF document
            return render(
                request,
                "benchmark/report.html",
                {
                    "team": "blue",
                    "first_tool": first_tool,
                    "second_tool": second_tool,
                },
            )
        else:
            messages.error(request, _("Formulaire invalide."))
    else:
        return redirect(reverse("customer_blue"))
    pass


@login_required
@user_passes_test(is_member_customers)
def benchmark_red(request):
    pass
