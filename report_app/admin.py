from django.contrib import admin

from .models import Task, SubTask, Unit, Activity, ActivityImages


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'child_category']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent_category']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['task', 'sub_task', 'name', 'slug', 'id',
                    'description', 'created', 'duration']
    list_filter = ['name', 'created']
    list_editable = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ActivityImages)
class ActivityImagesAdmin(admin.ModelAdmin):
    list_display = ['name']
