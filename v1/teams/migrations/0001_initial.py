# Generated by Django 3.1.1 on 2020-10-11 22:18

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contributors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeamContributor',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_lead', models.BooleanField(default=False)),
                ('pay_per_day', models.PositiveIntegerField()),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contributors.contributor')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
            options={
                'unique_together': {('team', 'contributor')},
            },
        ),
        migrations.AddField(
            model_name='team',
            name='contributors',
            field=models.ManyToManyField(through='teams.TeamContributor', to='contributors.Contributor'),
        ),
    ]
