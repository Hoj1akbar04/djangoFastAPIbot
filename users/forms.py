from django.contrib.auth.models import User
from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100)