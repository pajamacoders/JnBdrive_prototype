# from django import forms
from django.forms import ModelForm
from item_log.models import *


# class PartsCreateForm(forms.Form):
#     serial = forms.CharField(max_length=200, label="시리얼")
#     # category=forms.InlineForeignKeyField(PartsType)
#     sender = forms.EmailField()

class PartsCreateForm(ModelForm):
    class Meta:
        model = Parts
        fields = '__all__'