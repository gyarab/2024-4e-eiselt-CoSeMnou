from django.contrib import admin
from .models import School

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'min_czech_score', 'min_math_score', 'contact_email', 'phone_number', 'link')

admin.site.register(School, SchoolAdmin)

