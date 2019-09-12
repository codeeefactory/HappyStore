# -*- coding: utf-8 -*-

from django import forms

class LoginForm(forms.Form):
    UserName = forms.CharField(label='نام کاربری', max_length=100)
    Password = forms.CharField(label='رمز عبور', max_length=1000)
