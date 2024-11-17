from django import forms
from blog.models import Form
from django.db import models

class FormForm(forms.ModelForm):
    class Meta:
        model=Form
        fields="__all__"


class SubjectForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    field = forms.CharField(max_length=255)
    degree = forms.CharField(max_length=255)
    subject = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=12)
    summery = forms.CharField(widget=forms.Textarea(
            attrs={"class": "form-control"}))
