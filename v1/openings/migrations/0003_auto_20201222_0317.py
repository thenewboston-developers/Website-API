# Generated by Django 3.1.3 on 2020-12-22 03:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('openings', '0002_opening_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opening',
            options={'ordering': ('created_date',)},
        ),
    ]
