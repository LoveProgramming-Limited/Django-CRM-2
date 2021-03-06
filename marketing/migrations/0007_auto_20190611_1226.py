# Generated by Django 2.1.7 on 2019-06-11 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('marketing', '0006_campaign_attachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignCompleted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('campaign',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='campaign_is_completed',
                                      to='marketing.Campaign')),
            ],
        ),
        migrations.AlterField(
            model_name='campaignopen',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='contact_campaign', to='marketing.Contact'),
        ),
    ]
