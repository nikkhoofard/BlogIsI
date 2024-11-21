from django import forms
from blog.models import Form
from django.db import models

class FormForm(forms.ModelForm):
    class Meta:
        model=Form
        fields="__all__"


class SubjectForm(forms.Form):
    first_name = forms.CharField(max_length=255,label="نام کوچک",
                                 widget=forms.TextInput(
                                     {'id':'first-name',
                                      }
                                 ))
    last_name = forms.CharField(max_length=255,label="نام خانوادگی",
                                 widget=forms.TextInput(
                                     {'id':'last-name',
                                      }
                                 ))
    field = forms.CharField(max_length=255,label="رشته",
                                 widget=forms.TextInput(
                                     {'id':'field',
                                      }
                                 ))
    degree = forms.CharField(max_length=255,label=" مقطع",
                                 widget=forms.TextInput(
                                     {'id':'degree',
                                      }
                                 ))
    subject = forms.CharField(max_length=255,label="موضوع ",
                                 widget=forms.TextInput(
                                     {'id':'subject',
                                      }
                                 ))
    phone_number = forms.CharField(max_length=12,label="شماره همراه",
                                 widget=forms.TextInput(
                                     {'id':'phone-number',
                                      }
                                 ))
    summery = forms.CharField(widget=forms.Textarea(
           attrs={"class": "form-control"}))
