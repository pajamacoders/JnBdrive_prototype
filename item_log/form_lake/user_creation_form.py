
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationFormWrap(forms.ModelForm):
    username=forms.CharField(error_messages={'필수':" 사용자 아이디를 입력해주세요."}, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}))
    password=forms.CharField(error_messages={'필수':" 비밀번호를 입력해주세요."}, widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'}), label='비밀번호') #(attrs={'type': 'password', 'class': 'form-control'})
    re_password=forms.CharField(error_messages={'필수':" 비밀번호를 입력해주세요."}, widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'}), label='비밀번호 확인')
    email = forms.EmailField(required=False, label="이메일", widget=forms.EmailInput(attrs={'type': 'email', 'class': 'form-control'})) #help_text='A valid email address, please.'
    first_name=forms.CharField(required=False,widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}), label='이름')
    last_name=forms.CharField(required=False, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}), label='성')
    is_staff =forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-check-input'}), label='관리자',
    help_text='(관리자 페이지 접근을 허가하려면 체크 하십시오.)')

    class Meta:
        model=User
        fields=['username', 'password', 'email', 'first_name', 'last_name', 'is_staff']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean(self):                                                         
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        username = cleaned_data.get('username')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        is_staff = cleaned_data.get('is_staff')
        if password and re_password:
            if password != re_password :
                self.add_error('re_password', '비밀번호가 일치하지 않습니다.')
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


    
    