# Generated by Django 5.1.2 on 2024-10-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='city',
        ),
        migrations.RemoveField(
            model_name='school',
            name='postal_code',
        ),
        migrations.AddField(
            model_name='school',
            name='link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
