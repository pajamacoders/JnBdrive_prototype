

from django import forms
from item_log.models import PartsType

class PartsTypeUpdateForm(forms.ModelForm):

    class Meta:
        model = PartsType
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        }
