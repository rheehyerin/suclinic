from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator

class SignupForm(UserCreationForm):
    error_messages = {
        'password_mismatch' : "비밀번호가 일치하지 않습니다.",
        'required' : '모든 정보를 입력해주세요.',
        'unique' : '중복된 아이디입니다. 다시 입력해주세요',
    }
    password1 = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput,
        help_text="비밀번호 확인을 위한 입력창입니다."
    )
    email = forms.EmailField(
        label="이메일",
        validators=[EmailValidator(),],
        help_text="이메일을 형식에 맞게 입력해주세요. ex) example@suclinic.com"
        )

    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "email")

class UserForm(forms.ModelForm):
    username = forms.CharField(
        label='아이디',
        help_text='필수항목입니다. 30자 이내로 입력하세요. (알파벳, 숫자, @/./+/-/_만 가능)',
        max_length=30,
    )
    first_name = forms.CharField(
        label='이름',
        help_text='이름을 입력해주세요.',
        max_length=5,
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name')
