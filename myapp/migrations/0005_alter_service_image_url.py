# Generated by Django 4.1.13 on 2024-08-22 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_id_service_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image_url',
            field=models.TextField(blank=True, default='[]', max_length=200),
        ),
    ]