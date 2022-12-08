

from django import forms
from item_log.models import ProductionCompany

class ProductionCompanyUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs.keys() and kwargs['instance'] is not None:
            self.fields['business_number'].disabled = True
    class Meta:
        model = ProductionCompany
        fields = ['business_number', 'name', 'ceo', 'address', 'phone', 'insureance_company', 'insureance', 'start_date', 'end_date']
        widgets = {
            'business_number':forms.TextInput(attrs={'type': 'text', 'class': 'form-control col-lg-*'}),
            'name':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'ceo':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'address':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'phone':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'insureance_company':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'insureance':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'start_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
        }
    def _post_clean(self):
        super()._post_clean()
        if self._errors:
            for key in self._errors.keys():
                if 'already exists.' in self._errors[key][0]:
                    self._errors[key][0]=f'동일 사업자 번호를 가진 업체가 존재합니다.'
        
        if self.cleaned_data['start_date'] and self.cleaned_data['end_date']:
            if self.cleaned_data['start_date']> self.cleaned_data['end_date']:
                self.add_error('end_date', '보험 만기일은 시작일 보다 빠를 수 없습니다.')