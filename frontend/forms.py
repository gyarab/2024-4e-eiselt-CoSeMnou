from django import forms
from .models import School

class CompareForm(forms.Form):
    name = forms.CharField(label="Jméno", max_length=100)
    czech_score = forms.IntegerField(label="Body z češtiny", min_value=0, max_value=50)
    math_score = forms.IntegerField(label="Body z matematiky", min_value=0, max_value=50)

    # Výběr škol z databáze
    schools = School.objects.all()
    SCHOOL_CHOICES = [(school.name, school.name) for school in schools]

    first_choice = forms.ChoiceField(label="První volba", choices=SCHOOL_CHOICES)
    second_choice = forms.ChoiceField(label="Druhá volba", choices=SCHOOL_CHOICES)

