

from django import forms
from item_log.models import Reducer

class ReducerUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs.keys():
            self.fields['serial'].disabled = True
        else:
            self.fields['category'].initial='감속기'
    class Meta:
        model = Reducer
        fields = ['serial', 'category', 'production_date', 'discard_date', 'model_serial', 'gear_ratio']
        widgets = {
            'serial':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'category': forms.Select(attrs={'class':'form-select form-select-md mb-3'}),
            'production_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control','id':'inputGroup-sizing-sm'}),
            'discard_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
            'model_serial': forms.Select(attrs={'class':'form-select form-select-md mb-3'}),
            'gear_ratio':forms.NumberInput(attrs={'class': 'form-control', 'id':"floatingInput"})
        }
