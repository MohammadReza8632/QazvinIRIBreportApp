# Generated by Django 4.0.10 on 2023-10-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_app', '0007_alter_activity_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
