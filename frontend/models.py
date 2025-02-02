# frontend/models.py
from django.db import models

# frontend/models.py
class School(models.Model):
    name = models.CharField(max_length=100)   # Název školy 
    image = models.ImageField(upload_to='images/')  # Změna cesty pro obrázky
    address = models.CharField(max_length=255)  # Adresa školy
    link = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)  # Popis školy
    contact_email = models.EmailField(blank=True)  # Kontaktní e-mail
    phone_number = models.CharField(max_length=20, blank=True)  # Telefonní číslo

    def __str__(self):
        return self.name  # Název školy se bude zobrazovat v administraci
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    czech_score = models.IntegerField()  # Body z češtiny
    math_score = models.IntegerField()   # Body z matematiky
    first_choice = models.ForeignKey('School', related_name='first_choice_students', on_delete=models.CASCADE)
    second_choice = models.ForeignKey('School', related_name='second_choice_students', on_delete=models.CASCADE)

    def total_score(self):
        return self.czech_score + self.math_score

    def __str__(self):
        return self.name


class ExamResult(models.Model):
    student_name = models.CharField(max_length=100)
    czech_score = models.IntegerField()
    math_score = models.IntegerField()
    date_taken = models.DateField()

    def total_score(self):
        return self.czech_score + self.math_score

    def __str__(self):
        return f"{self.student_name} - {self.total_score()}"
