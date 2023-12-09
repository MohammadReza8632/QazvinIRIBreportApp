# Generated by Django 4.0.10 on 2023-11-16 09:42

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import report_app.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveIndex(
            model_name='activity',
            name='report_app__id_da36f9_idx',
        ),
        migrations.RemoveIndex(
            model_name='activity',
            name='report_app__name_id_aede87_idx',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='price',
        ),
        migrations.AddField(
            model_name='activity',
            name='colleague',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=django.contrib.auth.models.User),
        ),
        migrations.AddField(
            model_name='activity',
            name='shamsi',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='str_user',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activityimages',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='activity',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=100, verbose_name=report_app.models.Unit),
        ),
        migrations.AlterField(
            model_name='activity',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='sub_task',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=report_app.models.SubTask),
        ),
        migrations.AlterField(
            model_name='activity',
            name='task',
            field=models.CharField(max_length=100, verbose_name=report_app.models.Task),
        ),
        migrations.AddIndex(
            model_name='activity',
            index=models.Index(fields=['id'], name='report_app__id_7bf2ef_idx'),
        ),
        migrations.AddIndex(
            model_name='activity',
            index=models.Index(fields=['name'], name='report_app__name_337c41_idx'),
        ),
    ]