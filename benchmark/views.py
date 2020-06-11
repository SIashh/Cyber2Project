from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.template.loader import render_to_string
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

from io import BytesIO
from json import load
from PyPDF2 import PdfFileMerger, PdfFileReader
from xhtml2pdf import pisa
import os.path


def is_member_staff(user):
    return user.groups.filter(name="staff").exists()

def is_member_customers(user):
    return user.groups.filter(name__in=["staff", "customers"]).exists()

def customer_has_weighted_blue(user):
    return user.id in [bw.customer_id for bw in BlueWeight.objects.all()]

def customer_has_weighted_red(user):
    return user.id in [rw.customer_id for rw in RedWeight.objects.all()]

def staff_valid_data(team, form):
    # DB data
    customers = [u.id for u in User.objects.filter(groups__name="customers")]
    tools = [t.id for t in Tool.objects.all()]
    if team == "blue":
        notes = [(bn.customer_id, bn.tool_id) for bn in BlueNote.objects.all()]
    elif team == "red":
        notes = [(rn.customer_id, rn.tool_id) for rn in RedNote.objects.all()]

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
                    compatibilite_avec_outils_externes=form.cleaned_data.get(
                        "compatibilite_avec_outils_externes"
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
            customers_blueweights = [
                bw.customer_id for bw in BlueWeight.objects.all()
            ]
            customer = request.user.id
            if customer not in customers_blueweights:
                # No, Insert in DB
                weight = BlueWeight(
                    customer_id=customer,
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
                weight.save()
                messages.success(request, _("Pondération enregistrée ! Votre rapport de benchmarking Blue team est disponible dans votre profil !"))
                return redirect(reverse("profile"))
            else:
                # Yes, update in DB
                weight = BlueWeight.objects.filter(
                    customer_id=customer
                ).update(
                    detection=form.cleaned_data.get("capacite_d_analyse"),
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
    if request.method == "POST":
        form = CustomerRedForm(data=request.POST)
        if form.is_valid():
            # Is there already an entry in DB?
            customers_redweights = [
                rw.customer_id for rw in RedWeight.objects.all()
            ]
            customer = request.user.id
            if customer not in customers_redweights:
                # No, Insert in DB
                weight = RedWeight(
                    customer_id=customer,
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
                    compatibilite_avec_outils_externes=form.cleaned_data.get(
                        "compatibilite_avec_outils_externes"
                    ),
                )
                weight.save()

                # TODO: Generate red team benchmarking here

                messages.success(request, _("Pondération enregistrée !"))
                return redirect(reverse("customer_red"))
            else:
                # Yes, update in DB
                weight = RedWeight.objects.filter(customer_id=customer).update(
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
                    compatibilite_avec_outils_externes=form.cleaned_data.get(
                        "compatibilite_avec_outils_externes"
                    ),
                )
                messages.success(request, _("Pondération mise à jour !"))
                return redirect(reverse("customer_red"))
        else:
            messages.error(request, _("Formulaire invalide."))
            return redirect(reverse("customer_red"))
    else:
        form = CustomerRedForm()
        return render(
            request, "benchmark/customer.html", {"team": "red", "form": form}
        )


@login_required
@user_passes_test(is_member_customers)
def benchmark_blue(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cover_filename = os.path.join(BASE_DIR, 'castle/static/cover_page.pdf')
    report_filename = os.path.join(BASE_DIR, 'castle/static/report.pdf')
    blue_criteria_filename = os.path.join(BASE_DIR, 'castle/static/blue.json')


    # Redirect user if he has not completed weighting
    if not customer_has_weighted_blue(request.user):
        return redirect(reverse('profile'))

    # Get customer's notes in a dict
    bns = BlueNote.objects.filter(customer_id=request.user.id)
    notes = {}
    for bn in bns:
        notes[bn.tool_id] = {}
        for criterion in CRITERIA_BLUE.keys():
            notes[bn.tool_id][criterion] = str(getattr(bn, criterion))

    # Get customer's weights in a dict
    bw = BlueWeight.objects.get(customer_id=request.user.id)
    weights = {}
    for criterion in CRITERIA_BLUE.keys():
        weights[criterion] = getattr(bw, criterion)
    
    # For each team, for each tool, compute the total according to notes and weights and put it in a dict
    totals = {}
    for tool_id in notes.keys():
        totals[tool_id] = 0
        for criterion in CRITERIA_BLUE.keys():
            # Note is the sum of note*weight for each criterion
            note = notes[tool_id][criterion]
            weight = weights[criterion]
            totals[tool_id] += int(note)*weight
    
    # Which tool is the best?
    best_tool = list(totals.keys())[0]
    for tool_id in totals.keys():
        if totals[tool_id] > totals[best_tool]:
            best_tool = tool_id

    with open(blue_criteria_filename) as blue_criteria_file:
        blue_criteria = load(blue_criteria_file)

    # Filtering data
    all_tools = Tool.objects.all()
    notes_first_tool = list(notes.values())[0]
    notes_second_tool = list(notes.values())[1]
    name_first_tool = all_tools[list(notes.keys())[0] - 1].name
    name_second_tool = all_tools[list(notes.keys())[1] - 1].name

    # Generate HTML document
    html = render_to_string('benchmark/report_blue.html', {
        'first_tool': {'name': name_first_tool, 'notes': notes_first_tool},
        'second_tool': {'name': name_second_tool, 'notes': notes_second_tool},
        'blue_criteria': blue_criteria,
        'notes': notes,
        'weights': weights,
        'totals': totals,
        'best_tool': Tool.objects.get(id=best_tool).name.title()
    })

    # Convert HTML to PDF
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')), result)

    # Opening the report's first page and merging with results
    merged_pdfs = PdfFileMerger()
    merged_pdfs.append(PdfFileReader(cover_filename, 'rb'))
    pdf_content = BytesIO(result.getvalue())
    merged_pdfs.append(PdfFileReader(pdf_content))

    # Writing the report and printing it
    merged_pdfs.write(report_filename)

    if not pdf.err:
        return FileResponse(open(report_filename, 'rb'))
    else:
        messages.error(request, _("Erreur lors de la génération du rapport."))
        return redirect(reverse("profile"))


@login_required
@user_passes_test(is_member_customers)
def benchmark_red(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cover_filename = os.path.join(BASE_DIR, 'castle/static/cover_page.pdf')
    report_filename = os.path.join(BASE_DIR, 'castle/static/report.pdf')
    red_criteria_filename = os.path.join(BASE_DIR, 'castle/static/red.json')

    # Redirect user if he has not completed weighting
    if not customer_has_weighted_red(request.user):
        return redirect(reverse('profile'))

    # Get customer's notes in a dict
    rns = RedNote.objects.filter(customer_id=request.user.id)
    notes = {}
    for rn in rns:
        notes[rn.tool_id] = {}
        for criterion in CRITERIA_RED.keys():
            notes[rn.tool_id][criterion] = str(getattr(rn, criterion))

    # Get customer's weights in a dict
    rw = RedWeight.objects.get(customer_id=request.user.id)
    weights = {}
    for criterion in CRITERIA_RED.keys():
        weights[criterion] = getattr(rw, criterion)
    
    # For each team, for each tool, compute the total according to notes and weights and put it in a dict
    totals = {}
    for tool_id in notes.keys():
        totals[tool_id] = 0
        for criterion in CRITERIA_RED.keys():
            # Note is the sum of note*weight for each criterion
            note = notes[tool_id][criterion]
            weight = weights[criterion]
            totals[tool_id] += int(note)*weight
    
    # Which tool is the best?
    best_tool = list(totals.keys())[0]
    for tool_id in totals.keys():
        if totals[tool_id] > totals[best_tool]:
            best_tool = tool_id

    with open(red_criteria_filename) as red_criteria_file:
        red_criteria = load(red_criteria_file)

    all_tools =Tool.objects.all()
    notes_first_tool = list(notes.values())[0]
    notes_second_tool = list(notes.values())[1]
    name_first_tool = all_tools[list(notes.keys())[0] - 1].name
    name_second_tool = all_tools[list(notes.keys())[1] - 1].name

    # Generate HTML document
    html = render_to_string('benchmark/report_red.html', {
        'first_tool': {'name': name_first_tool, 'notes': notes_first_tool},
        'second_tool': {'name': name_second_tool, 'notes': notes_second_tool},
        'red_criteria': red_criteria,
        'notes': notes,
        'weights': weights,
        'totals': totals,
        'best_tool': Tool.objects.get(id=best_tool).name.title()
    })

    # Convert HTML to PDF
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')), result)

    # Opening the report's first page and merging with results
    merged_pdfs = PdfFileMerger()
    merged_pdfs.append(PdfFileReader(cover_filename, 'rb'))
    pdf_content = BytesIO(result.getvalue())
    merged_pdfs.append(PdfFileReader(pdf_content))

    # Writing the report and printing it
    merged_pdfs.write(report_filename)

    if not pdf.err:
        return FileResponse(open(report_filename, 'rb'))
    else:
        messages.error(request, _("Erreur lors de la génération du rapport."))
        return redirect(reverse("profile"))
