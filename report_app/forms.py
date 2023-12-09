from django import forms
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from .models import Activity, ActivityImages
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from .validators import validate_file_size

class ActivityForm(forms.ModelForm):
    more_images = forms.ImageField(required=False, validators=[validate_file_size], widget=forms.FileInput(attrs={
        "class": "form-control",
        "multiple": True,
    }))

    class Meta:
        model = Activity
        fields = ['task', 'sub_task', 'name', 'image', 'created', 'duration', 'colleague', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2, 'cols': 38}),
        }

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields["created"] = JalaliDateField(widget=AdminJalaliDateWidget, )
        self.fields['created'].widget.attrs['placeholder'] = "ثبت تاریخ"
        self.fields['task'].widget.attrs['placeholder'] = "انتخاب عنوان کلی فعالیت"
        self.fields['task'].widget.attrs['id'] = "main-activity-field"
        self.fields['sub_task'].widget.attrs['placeholder'] = "انتخاب فعالیت"
        self.fields['sub_task'].widget.attrs['id'] = "sub-main-activity-field"
        self.fields['name'].widget.attrs['placeholder'] = "انتخاب واحد"
        self.fields['name'].widget.attrs['id'] = "unit-activity-field"
        self.fields['duration'].widget.attrs['placeholder'] = "مدت زمان انجام فعالیت(ساعت)"
        self.fields['colleague'].widget.attrs['placeholder'] = "انتخاب همکار"
        self.fields['colleague'].widget.attrs['id'] = "colleague-activity-field"
        self.fields['description'].widget.attrs['placeholder'] = "   توضیحات "


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_class', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_class', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_class', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
