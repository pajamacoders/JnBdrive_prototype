

from django import forms
from item_log.models import FaultHistory

class FaultHistoryUpdateForm(forms.ModelForm):
    class Meta:
        model = FaultHistory
        fields = '__all__' #['id', 'check_type', 'date', 'effective_duration', 'inspection_agency', 'inspector', 'result', 'part', 'product']
        widgets = {
            'fault_type':forms.TextInput(attrs={'type': 'text', 'class': 'form-control mb-3'}),
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
            'cause': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'repair_company': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'parts': forms.Select(attrs={'class':'form-select', 'id':'select2_1st'}),#, 'id':'part_list'form-select-md mb-3
        }
