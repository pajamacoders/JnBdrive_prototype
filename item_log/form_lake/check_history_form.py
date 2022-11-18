

from django import forms
from .custom_widget import AutoCompleteWidget
from item_log.models import CheckHistory

class CheckHistoryUpdateForm(forms.ModelForm):
    class Meta:
        model = CheckHistory
        fields = ['id', 'check_type', 'date', 'effective_duration', 'inspection_agency', 'inspector', 'result', 'part', 'product']
        widgets = {
            'check_type':forms.TextInput(attrs={'type': 'text', 'class': 'form-control mb-3'}),
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
            'effective_duration': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'inspection_agency': forms.Select(attrs={'class':'form-select form-select-md mb-3'}),
            'inspector':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'result':forms.Select(attrs={'class':'form-select form-select-md mb-3'}),
            'part': forms.Select(attrs={'class':'form-control form-select form-select-md mb-6', 'id':'part_list'}),
            'product': forms.Select(attrs={'class':'form-control form-select form-select-md mb-6', 'id':'product_list'}),
        }
