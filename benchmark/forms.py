from django.forms import ChoiceField, Form, Select, RadioSelect
from django.urls import reverse
from crispy_forms.bootstrap import FormActions, InlineField, InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, ButtonHolder, Div, Fieldset, HTML, Layout, Submit

CRITERIA_BLUE = { # Ajouter un clé pour chaque nouveau critère, associé à son poids par défaut  
    'prix': 4,
    'argent': 3,
    'moula': 2,
    'crit1': 3,
    'crit2': 1
}

CRITERIA_RED = {
	'prix': 4
}

CHOICES = (
    (1, "Niveau 1 (moins bonne notation)"),
    (2, "Niveau 2"),
    (3, "Niveau 3"),
    (4, "Niveau 4"),
    (5, "Niveau 5 (meilleure notation)")
)

class CustomerBlueForm(Form):
        # Ajouter ici un champ pour chaque ligne de CRITERIA personnalisable par le client
        prix = ChoiceField(widget=Select, choices=CHOICES, initial=CRITERIA_BLUE['prix'])
        argent = ChoiceField(widget=Select, choices=CHOICES, initial=CRITERIA_BLUE['argent'])
        moula = ChoiceField(widget=Select, choices=CHOICES, initial=CRITERIA_BLUE['moula'])

class CustomerRedForm(Form):
        prix = ChoiceField(widget=Select, choices=CHOICES, initial=CRITERIA_RED['prix'])

class StaffBlueForm(Form):
        capacité_d_analyse = ChoiceField(widget=Select(attrs={'class': 'mt-1'}), choices=CHOICES)
        détection = ChoiceField(widget=Select(attrs={'class': 'mt-1'}), choices=CHOICES)
        complexité_d_analyse = ChoiceField(widget=Select(attrs={'class': 'mt-1'}), choices=CHOICES)
        export_des_résultats = ChoiceField(widget=Select(attrs={'class': 'mt-1'}), choices=CHOICES)
        création_de_règles = ChoiceField(widget=Select(attrs={'class': 'mt-1'}), choices=CHOICES)
        export_de_fichier_suspect = ChoiceField(widget=Select(attrs={'class': 'mt-1'}), choices=CHOICES)
        prévention = ChoiceField(widget=Select(attrs={'class': 'mt-1'}), choices=CHOICES)

