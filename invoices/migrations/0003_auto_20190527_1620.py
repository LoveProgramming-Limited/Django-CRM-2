# Generated by Django 2.1.7 on 2019-05-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('invoices', '0002_auto_20190524_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='details',
            field=models.TextField(blank=True, null=True, verbose_name='Details'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
