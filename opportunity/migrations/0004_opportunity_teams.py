# Generated by Django 2.2.4 on 2019-09-17 05:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('teams', '0003_auto_20190909_1621'),
        ('opportunity', '0003_auto_20190212_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='teams',
            field=models.ManyToManyField(related_name='oppurtunity_teams', to='teams.Teams'),
        ),
    ]
