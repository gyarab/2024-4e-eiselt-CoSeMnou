from django import forms
from .models import School

# formular porovnani skore + vyber skol
class CompareForm(forms.Form):
    name = forms.CharField(label="Jméno", max_length=100)
    czech_score = forms.IntegerField(label="Body z češtiny", min_value=0, max_value=50)
    math_score = forms.IntegerField(label="Body z matematiky", min_value=0, max_value=50)

     # ziskani vsech skol z databaze
    schools = School.objects.all()
     # definovani moznosti vyberu skoly
    SCHOOL_CHOICES = [("", "— Vyberte školu —")] + [(school.id, school.name) for school in schools]

    first_choice = forms.ChoiceField(label="První volba", choices=SCHOOL_CHOICES)
    second_choice = forms.ChoiceField(label="Druhá volba", choices=SCHOOL_CHOICES)
    third_choice = forms.ChoiceField(label="Třetí volba", choices=SCHOOL_CHOICES, required=False)

    # validace vyberu skol
    def clean(self):
        cleaned_data = super().clean()
        first_choice = cleaned_data.get("first_choice")
        second_choice = cleaned_data.get("second_choice")
        third_choice = cleaned_data.get("third_choice")

        # ?prvni 2 skoly?
        if not first_choice or not second_choice:
            self.add_error(None, "Musíte vybrat alespoň první a druhou školu.")

        # ?stejna 1. 2. skola?
        if first_choice == second_choice:
            self.add_error(None, "První a druhá volba nesmí být stejná škola.")

        # ?stejna 3. skola?
        if third_choice:
            if first_choice == third_choice:
                self.add_error(None, "První a třetí volba nesmí být stejná škola.")
            if second_choice == third_choice:
                self.add_error(None, "Druhá a třetí volba nesmí být stejná škola.")

        return cleaned_data