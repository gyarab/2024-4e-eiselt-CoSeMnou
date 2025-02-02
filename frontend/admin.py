from django.contrib import admin
from .models import School

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_email', 'phone_number', 'link')  # Pole viditelná v přehledu
    search_fields = ('name', 'address', 'contact_email')  # Vyhledávací pole
    list_filter = ('address',)  # Filtrování podle adresy
    fieldsets = (
        (None, {
            'fields': ('name', 'image', 'address', 'link', 'description', 'contact_email', 'phone_number')
        }),
    )
