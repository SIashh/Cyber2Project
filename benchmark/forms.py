from django.contrib.staticfiles.storage import staticfiles_storage
from django.forms import ChoiceField, Form, Select, RadioSelect
from django.urls import reverse
from crispy_forms.bootstrap import FormActions, InlineField, InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, ButtonHolder, Div, Fieldset, HTML, Layout, Submit

import os.path
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

blue = os.path.join(BASE_DIR, 'castle/static/blue.json')
red = os.path.join(BASE_DIR, 'castle/static/red.json')

CRITERIA_BLUE = json.load(open(blue))
CRITERIA_RED = json.load(open(red))

CHOICES = (
    (5, "Niveau 5 : Critère de poids majeur"),
    (4, "Niveau 4 : Critère de poids considérable"),
    (3, "Niveau 3 : Critère de poids important"),
    (2, "Niveau 2 : Critère de poids moyen"),
    (1, "Niveau 1 : Critère de poids faible")
)

class CustomerBlueForm(Form):
	# Ajouter ici un champ pour chaque entrée de "static/blue.json" personnalisable par le client
	detection = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_BLUE['detection']["weight"],
		label=CRITERIA_BLUE['detection']["label"],
		help_text=CRITERIA_BLUE['detection']["help_text"])
	capacite_d_analyse = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_BLUE['capacite_d_analyse']["weight"],
		label=CRITERIA_BLUE['capacite_d_analyse']["label"],
		help_text=CRITERIA_BLUE['capacite_d_analyse']["help_text"])
	complexite_d_analyse = ChoiceField(widget=Select,
		choices=CHOICES,
		initial=CRITERIA_BLUE['complexite_d_analyse']["weight"],
		label=CRITERIA_BLUE['complexite_d_analyse']["label"],
		help_text=CRITERIA_BLUE['complexite_d_analyse']["help_text"])
	export_des_resultats = ChoiceField(widget=Select,
		choices=CHOICES,
		initial=CRITERIA_BLUE['export_des_resultats']["weight"],
		label=CRITERIA_BLUE['export_des_resultats']["label"],
		help_text=CRITERIA_BLUE['export_des_resultats']["help_text"])
	creation_de_regles = ChoiceField(widget=Select,
		choices=CHOICES,
		initial=CRITERIA_BLUE['creation_de_regles']["weight"],
		label=CRITERIA_BLUE['creation_de_regles']["label"],
		help_text=CRITERIA_BLUE['creation_de_regles']["help_text"])
	export_de_fichier_suspect = ChoiceField(widget=Select,
		choices=CHOICES,
		initial=CRITERIA_BLUE['export_de_fichier_suspect']["weight"],
		label=CRITERIA_BLUE['export_de_fichier_suspect']["label"],
		help_text=CRITERIA_BLUE['export_de_fichier_suspect']["help_text"])
	prevention = ChoiceField(widget=Select,
		choices=CHOICES,
		initial=CRITERIA_BLUE['prevention']["weight"],
		label=CRITERIA_BLUE['prevention']["label"],
		help_text=CRITERIA_BLUE['prevention']["help_text"])

class CustomerRedForm(Form):
	# Ajouter ici un champ pour chaque entrée de "static/red.json" personnalisable par le client
	mise_a_jour = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['mise_a_jour']["weight"],
		label=CRITERIA_RED['mise_a_jour']["label"],
		help_text=CRITERIA_RED['mise_a_jour']["help_text"])
	capacite_de_detection = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['capacite_de_detection']["weight"],
		label=CRITERIA_RED['capacite_de_detection']["label"],
		help_text=CRITERIA_RED['capacite_de_detection']["help_text"])
	configuration = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['configuration']["weight"],
		label=CRITERIA_RED['configuration']["label"],
		help_text=CRITERIA_RED['configuration']["help_text"])
	rapidite_d_execution = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['rapidite_d_execution']["weight"],
		label=CRITERIA_RED['rapidite_d_execution']["label"],
		help_text=CRITERIA_RED['rapidite_d_execution']["help_text"])
	comsommation_de_ressources = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['comsommation_de_ressources']["weight"],
		label=CRITERIA_RED['comsommation_de_ressources']["label"],
		help_text=CRITERIA_RED['comsommation_de_ressources']["help_text"])
	explication_de_vulnerabilite = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['explication_de_vulnerabilite']["weight"],
		label=CRITERIA_RED['explication_de_vulnerabilite']["label"],
		help_text=CRITERIA_RED['explication_de_vulnerabilite']["help_text"])
	scope_de_scan = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['scope_de_scan']["weight"],
		label=CRITERIA_RED['scope_de_scan']["label"],
		help_text=CRITERIA_RED['scope_de_scan']["help_text"])
	flexibilite = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['flexibilite']["weight"],
		label=CRITERIA_RED['flexibilite']["label"],
		help_text=CRITERIA_RED['flexibilite']["help_text"])
	communaute = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['communaute']["weight"],
		label=CRITERIA_RED['communaute']["label"],
		help_text=CRITERIA_RED['communaute']["help_text"])
	compatibilite_avec_outis_externes = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['compatibilite_avec_outis_externes']["weight"],
		label=CRITERIA_RED['compatibilite_avec_outis_externes']["label"],
		help_text=CRITERIA_RED['compatibilite_avec_outis_externes']["help_text"])
	

class StaffBlueForm(Form):
        capacité_d_analyse = ChoiceField(widget=Select(attrs={'class': 'mt-1'}), choices=CHOICES)
        détection = ChoiceField(widget=Select(attrs={'class': 'mt-1'}), choices=CHOICES)
        complexité_d_analyse = ChoiceField(widget=Select(attrs={'class': 'mt-1'}), choices=CHOICES)
        export_des_résultats = ChoiceField(widget=Select(attrs={'class': 'mt-1'}), choices=CHOICES)
        création_de_règles = ChoiceField(widget=Select(attrs={'class': 'mt-1'}), choices=CHOICES)
        export_de_fichier_suspect = ChoiceField(widget=Select(attrs={'class': 'mt-1'}), choices=CHOICES)
        prévention = ChoiceField(widget=Select(attrs={'class': 'mt-1'}), choices=CHOICES)


class StaffRedForm(Form):
	customer_id = ChoiceField(
		widget=Select,
		choices=(), # liste des ID clients
		label='ID client',
		help_text="Identifiant du client pour lequel les outils sont benchmarkés."
	)
	tool = ChoiceField(
		widget=Select,
		choices=(), # liste des tools red non notés
		label='Outil',
		help_text="Outil pour lequel les notes des critères ci-dessous vont s'appliquer."
	)

	# Ajouter ici un champ pour chaque entrée de "static/red.json"
	contexte = ChoiceField(
		widget=Select,
		# choices=CRITERIA_RED['contexte']['notes'], # ne fonctionne pas en l'état
		label=CRITERIA_RED['contexte']['label'],
		help_text=CRITERIA_RED['contexte']['help_text'])