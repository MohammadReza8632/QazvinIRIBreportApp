# Generated by Django 4.0.10 on 2023-10-23 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_app', '0009_alter_activity_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]