from django import forms
from .models import School

class CompareForm(forms.Form):
    name = forms.CharField(label="Jméno", max_length=100)
    czech_score = forms.IntegerField(label="Body z češtiny", min_value=0, max_value=50)
    math_score = forms.IntegerField(label="Body z matematiky", min_value=0, max_value=50)

    # Výběr škol z databáze + pomlčka pro "žádnou zvolenou školu"
    schools = School.objects.all()
    SCHOOL_CHOICES = [("", "— Vyberte školu —")] + [(school.id, school.name) for school in schools]

    first_choice = forms.ChoiceField(label="První volba", choices=SCHOOL_CHOICES)
    second_choice = forms.ChoiceField(label="Druhá volba", choices=SCHOOL_CHOICES)
    third_choice = forms.ChoiceField(label="Třetí volba", choices=SCHOOL_CHOICES, required=False)

    def clean(self):
        cleaned_data = super().clean()
        first_choice = cleaned_data.get("first_choice")
        second_choice = cleaned_data.get("second_choice")
        third_choice = cleaned_data.get("third_choice")

        # Kontrola, jestli uživatel nevybral pomlčku místo školy
        if first_choice == "" or second_choice == "":
            raise forms.ValidationError("Musíte vybrat alespoň první a druhou školu.")

        return cleaned_data
