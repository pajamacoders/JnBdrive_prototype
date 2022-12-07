

from django import forms
from item_log.models import SafetyDevice

class SafetyDeviceUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs.keys():
            self.fields['serial'].disabled = True
        else:
            self.fields['category'].initial='가바나'
    class Meta:
        model = SafetyDevice
        fields = ['serial', 'category', 'production_date', 'discard_date',  'capacity']
        widgets = {
            'serial':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'category': forms.Select(attrs={'class':'form-select form-select-md mb-3'}),
            'production_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control','id':'inputGroup-sizing-sm'}),
            'discard_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
            # 'model_serial': forms.Select(attrs={'class':'form-select form-select-md mb-3'}),
            'capacity':forms.NumberInput(attrs={'class': 'form-control', 'id':"floatingInput"})
        }
