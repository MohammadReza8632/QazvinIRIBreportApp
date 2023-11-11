from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from jalali_date import date2jalali, datetime2jalali
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    child_category = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return self.name


class SubTask(models.Model):
    parent_category = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task = models.CharField(Task, max_length=100)
    sub_task = models.CharField(SubTask,
                                null=True, blank=True, max_length=100)
    name = models.CharField(Unit, max_length=100)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    description = models.TextField(blank=True, max_length=1000)
    duration = models.PositiveIntegerField(null=True, blank=True)
    colleague = models.CharField(User, max_length=100, null=True)
    created = models.DateTimeField(default=timezone.now)
    shamsi = models.CharField(max_length=10, null=True)
    str_user = models.CharField(max_length=50, null=True)

    def get_jalali_date(self):
        return date2jalali(self.created)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Activity, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

        def __str__(self):
            return str(self.id)


class ActivityImages(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.activity.name
