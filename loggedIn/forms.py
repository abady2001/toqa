from dataclasses import field
from email.policy import default
from multiprocessing import AuthenticationError
from urllib import request
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.views.generic import UpdateView
from django.urls import path, reverse_lazy


username_validator = UnicodeUsernameValidator()

class creatNewUser (UserCreationForm):
    
    first_name = forms.CharField(max_length=12, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control p-2 mt-2 text-center '}),
                                 error_messages={'required': 'يجب إدخال الاسم الأول'})
    last_name = forms.CharField(max_length=12, required=True,
                                widget=(forms.TextInput(attrs={'class': 'form-control p-2 mt-2 text-center '})),
                                error_messages={'required': 'يجب إدخال اسم العائلة'})
    email = forms.EmailField(max_length=50,
                             widget=(forms.TextInput(attrs={'class': 'form-control p-2 mt-2 text-center '})),
                             error_messages={'required': 'يجب إدخال البريد الإلكتروني'})

    password1 = forms.CharField(
        widget=(forms.PasswordInput(
            attrs={'class': 'form-control p-2 mt-2 text-center '})))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control p-2 mt-2 text-center '}))

    username = forms.CharField(
        max_length=150,
        validators=[username_validator],
        widget=forms.TextInput(
            attrs={'class': 'form-control p-2 mt-2 text-center '}),
        error_messages={'unique': (
            "الاسم مُستخدم بالفعل")},
    )
    
    Nationality = forms.CharField(max_length=25, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control p-2 mt-2 text-center '}),
                                 error_messages={'required': 'يجب إدخال الجنسية'})
    
    def __init__(self, *args, **kwargs):
        super(creatNewUser, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'اسم المستخدم (باللغة الإنجليزية) '
        self.fields['email'].label = 'البريد الإلكتروني'
        self.fields['password1'].label = 'كلمة المرور '
        self.fields['password2'].label = 'تحقق من كلمة المرور'
        self.fields['first_name'].label = 'الاسم الأول'
        self.fields['last_name'].label = 'اسم العائلة'
        self.fields['Nationality'].label = 'الجنسية '

        for field in self.fields:
            self.fields[field].help_text = ''

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',
                  'first_name', 'last_name']
        fields += UserCreationForm.Meta.fields + ( 'Nationality',)
