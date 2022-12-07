

from django import forms
from .custom_widget import AutoCompleteWidget
from item_log.models import CheckHistory

class CheckHistoryUpdateForm(forms.ModelForm):
    class Meta:
        model = CheckHistory
        fields = ['id', 'check_type', 'date', 'effective_duration', 'inspection_agency', 'inspector', 'result', 'part', 'product']
        widgets = {
            'check_type':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class': 'form-control'}),
            'effective_duration': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'inspection_agency': forms.Select(attrs={'class':'form-select ','id':'select2_3rd'}),
            'inspector':forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'result':forms.Select(attrs={'class':'form-select', 'id':'select2_4th'}),
            'part': forms.Select(attrs={'class':'form-select', 'id':'select2_1st'}),
            'product': forms.Select(attrs={'class':'form-select', 'id':'select2_2nd'}),
        }

    def check_if_null_or_blank(self, key):
        """
        return True if key is null or blank
        """
        return True if key is None else False
    def _clean_form(self):                                                         
        cleaned_data = super().clean()
        part = cleaned_data.get('part')
        product = cleaned_data.get('product')
        if self.check_if_null_or_blank(part) and self.check_if_null_or_blank(product):
            self.add_error('product', '검사대상 제품 또는 부품 하나를 선택하십시오')
        elif not self.check_if_null_or_blank(part) and not self.check_if_null_or_blank(product):
            self.add_error('product', '검사대상은 제품 또는 부품 하나만 선택할 수 있습니다.')
        else:
            pass
        # if  and re_password:
        #     if password != re_password :
        #         self.add_error('re_password', '비밀번호가 일치하지 않습니다.')
            # else:
                # user = User(
                #     username=username,
                #     first_name=first_name,
                #     last_name=last_name,
                #     email = email,
                #     password = make_password(password),
                #     is_staff=is_staff
                # )
                # user.save()
                # self.email = user.email
        return cleaned_data
