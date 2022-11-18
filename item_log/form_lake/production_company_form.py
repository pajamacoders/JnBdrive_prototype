

from django import forms
from item_log.models import ProductionCompany

class ProductionCompanyUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs.keys():
            self.fields['business_number'].disabled = True
    class Meta:
        model = ProductionCompany
        fields = ['business_number', 'name', 'ceo', 'address', 'phone', 'insureance_company', 'insureance', 'start_date', 'end_date']
        widgets = {
            'business_number':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'name':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'ceo':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'address':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'phone':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'insureance_company':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'insureance':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'start_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control','id':'inputGroup-sizing-sm'}),
            'end_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
        }
