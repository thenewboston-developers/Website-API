# Generated by Django 3.1.3 on 2021-03-10 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_auto_20210219_0551'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectMember',
            fields=[
                ('teammember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teams.teammember')),
            ],
            options={
                'abstract': False,
            },
            bases=('teams.teammember',),
        ),
        migrations.CreateModel(
            name='ProjectTeam',
            fields=[
                ('team_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teams.team')),
                ('external_url', models.URLField(blank=True, max_length=500, null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('teams.team',),
        ),
        migrations.RemoveField(
            model_name='team',
            name='responsibilities',
        ),
        migrations.AddField(
            model_name='team',
            name='github',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='slack',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='teammember',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='CoreTeam',
            fields=[
                ('team_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teams.team')),
                ('responsibilities', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('teams.team',),
        ),
        migrations.DeleteModel(
            name='SlackChannel',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='pay_per_day',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='team',
        ),
        migrations.CreateModel(
            name='CoreMember',
            fields=[
                ('teammember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teams.teammember')),
                ('pay_per_day', models.PositiveIntegerField(default=2800)),
            ],
            options={
                'abstract': False,
            },
            bases=('teams.teammember',),
        ),
    ]
