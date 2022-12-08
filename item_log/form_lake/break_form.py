

from django import forms
from item_log.models import Break

class BreakUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs.keys() and kwargs['instance'] is not None:
            self.fields['serial'].disabled = True
        self.fields['category'].initial='브레이크'
    class Meta:
        model = Break
        fields = ['serial', 'category', 'production_date', 'discard_date',  'torque']
        widgets = {
            'serial':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'category': forms.Select(attrs={'class':'form-select form-select-md mb-3'}),
            'production_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control','id':'inputGroup-sizing-sm'}),
            'discard_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
            # 'model_serial': forms.Select(attrs={'class':'form-select form-select-md mb-3'}),
            'torque':forms.NumberInput(attrs={'class': 'form-control', 'id':"floatingInput"})
        }

    def _post_clean(self):
        super()._post_clean()
        if self._errors:
            for key in self._errors.keys():
                if 'already exists.' in self._errors[key][0]:
                    self._errors[key][0]=f'입력한 시리얼 번호를 가진 브레이크가 이미 존재합니다.'

        if self.cleaned_data['production_date'] and self.cleaned_data['discard_date']:
            if self.cleaned_data['production_date']> self.cleaned_data['discard_date']:
                self.add_error('discard_date', '폐기 일은 생성일 보다 빠를수 없습니다.')