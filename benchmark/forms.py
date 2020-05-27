from django.forms import ChoiceField, Form, Select
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
    (1, "Pas du tout important"),
    (2, "Pas important"),
    (3, "Important"),
    (4, "Très important")
)

class CustomerBlueForm(Form):
        # Ajouter ici un champ pour chaque ligne de CRITERIA personnalisable par le client
        prix = ChoiceField(widget=Select, choices=CHOICES, initial=CRITERIA_BLUE['prix'])
        argent = ChoiceField(widget=Select, choices=CHOICES, initial=CRITERIA_BLUE['argent'])
        moula = ChoiceField(widget=Select, choices=CHOICES, initial=CRITERIA_BLUE['moula'])

class CustomerRedForm(Form):
        prix = ChoiceField(widget=Select, choices=CHOICES, initial=CRITERIA_RED['prix'])
