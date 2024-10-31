# frontend/models.py
from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)   # Název školy 
    image = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=255)  # Adresa školy
    link= models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)  # Popis školy
    contact_email = models.EmailField(blank=True)  # Kontaktní e-mail
    phone_number = models.CharField(max_length=20, blank=True)  # Telefonní číslo

    def __str__(self):
        return self.name  # Název školy se bude zobrazovat v administraci

class ExamResult(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.IntegerField()
    min_score_math = models.IntegerField()
    min_score_czech = models.IntegerField()
