

from django import forms
from item_log.models import Product
from django.core.exceptions import ValidationError
from django.utils.text import capfirst, get_text_list

id2label = {
    'safety_device':'가바나',
    'motor':'모터',
    'brake':'브레이크',
    'reducer':'감속기'
}
class ProductUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'model': forms.Select(attrs={'class':'form-select form-select-md mb-3', 'id':'select2_1st'}),
            'serial':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'production_company': forms.Select(attrs={'class':'form-select form-select-md mb-3', 'id':'select2_2nd'}),
            'production_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control','id':'inputGroup-sizing-sm'}),
            'discard_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
            'motor': forms.Select(attrs={'class':'form-select form-select-md mb-3', 'id':'select2_3rd'}),
            'brake': forms.Select(attrs={'class':'form-select form-select-md mb-3', 'id':'select2_4th'}),
            'safety_device': forms.Select(attrs={'class':'form-select form-select-md mb-3', 'id':'select2_5th'}),
            'reducer': forms.Select(attrs={'class':'form-select form-select-md mb-3', 'id':'select2_6th'}),
        }
    
    def _post_clean(self):
        super()._post_clean()
        if self._errors:
            for key in self._errors.keys():
                if 'already exists.' in self._errors[key][0]:
                    self._errors[key][0]=f'지정한 {id2label[key]}는 다른 제품에서 사용 중 입니다.'
