# Generated by Django 4.0.10 on 2023-11-14 09:46

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_app', '0019_activity_colleague'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='colleague',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
