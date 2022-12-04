

from django import forms
from item_log.models import Product

class ProductUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'model': forms.Select(attrs={'class':'form-select form-select-md mb-3'}),
            'serial':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'production_company': forms.Select(attrs={'class':'form-select form-select-md mb-3'}),
            'production_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control','id':'inputGroup-sizing-sm'}),
            'discard_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
        }
