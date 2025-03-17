# Generated by Django 5.1.2 on 2025-03-17 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_alter_school_address_alter_school_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='third_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_choice_students', to='frontend.school'),
        ),
    ]
