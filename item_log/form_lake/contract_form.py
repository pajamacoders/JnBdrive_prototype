

from django import forms
from item_log.models import Contract

class ContractUpdateForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
        widgets = {
            'site_name':forms.TextInput(attrs={'type': 'text', 'class': 'form-control mb-6'}),
            'address':forms.TextInput(attrs={'type': 'text', 'class': 'form-control mb-6'}),
            'part': forms.Select(attrs={'class':'form-control form-select form-select-md mb-6', 'id':'select2_1st'}),
            'product': forms.Select(attrs={'class':'form-control form-select form-select-md mb-6', 'id':'select2_2nd'}),
            'num_floors':forms.NumberInput(attrs={'class': 'form-control', 'id':"typeNumber"}),
            'num_basements':forms.NumberInput(attrs={'class': 'form-control', 'id':"typeNumber"}),
            'installation_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
            'next_check_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
            'withdrawal_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
            'safety_checker': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'safety_checker_higher_date':forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
            'safety_checker_phone': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'safety_edu_comp_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
            'management_company':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'management_comp_phone':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'subcontract_company':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'subcontract_comp_phone':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),   
        }
