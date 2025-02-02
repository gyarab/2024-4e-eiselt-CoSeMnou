from django import forms
from .models import Student, School

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'czech_score', 'math_score', 'first_choice', 'second_choice']
        widgets = {
            'first_choice': forms.Select(attrs={'class': 'form-control'}),
            'second_choice': forms.Select(attrs={'class': 'form-control'}),
        }
