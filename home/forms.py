from multiprocessing import AuthenticationError
from django import forms
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


username_validator = UnicodeUsernameValidator()



class loginForm (AuthenticationForm):

    password = forms.CharField(
        widget=(forms.PasswordInput(
            attrs={'class': 'form-control p-2 mt-2 '})))

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={'class': 'form-control p-2 mt-2'})
    
    )
    error_messages = {
        'invalid_login': (
            "هناك خطب ما في اسم المستخدم أو كلمة المرور"
        )}

    def __init__(self, *args, **kwargs):
        super(loginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "اسم المستخدم (باللغة الإنجليزية)"
        self.fields['password'].label = 'كلمة المرور '

        for field in self.fields:
            self.fields[field].help_text = ''



