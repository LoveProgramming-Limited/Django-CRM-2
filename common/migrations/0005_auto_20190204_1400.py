# Generated by Django 2.1.5 on 2019-02-04 08:30

from django.db import migrations, models


def generate_document_status(apps, schema_editor):
    Document = apps.get_model("common", "Document")
    for document in Document.objects.all():
        document.status = 'active'
        document.save()


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0004_attachments_case'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-is_active']},
        ),
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active',
                                   max_length=64),
        ),
        migrations.RunPython(generate_document_status)
    ]
