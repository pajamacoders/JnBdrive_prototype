

from django import forms
from item_log.models import ModelType

class ModelTypeUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs.keys():
            self.fields['model'].disabled = True
    class Meta:
        model = ModelType
        fields = ['model', 'type', 'load_weight', 'operation_section', 'capacity', 'rated_speed']
        widgets = {
            'model':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'type': forms.Select(attrs={'class':'form-select form-select-md mb-3'}),
            'load_weight': forms.NumberInput(attrs={'class': 'form-control', 'id':"typeNumber"}),
            'operation_section': forms.NumberInput(attrs={'class': 'form-control', 'id':"typeNumber"}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'id':"typeNumber"}),
            'rated_speed':forms.NumberInput(attrs={'class': 'form-control', 'id':"typeNumber"})
        }
