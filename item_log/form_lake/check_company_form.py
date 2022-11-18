

from django import forms
from item_log.models import CheckCompany

class CheckCompanyUpdateForm(forms.ModelForm):

    class Meta:
        model = CheckCompany
        fields = ['id','name']
        widgets = {
            'name':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'})
        }
