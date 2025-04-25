from django import forms
from django.forms import fields
from .models import User

class Signup(forms.ModelForm):
  username = forms.CharField(label="Username required", widget=forms.TextInput(
    attrs={
      'class': 'form-control bg-light'
    }
  ))

  first_name = forms.CharField(label="First name required", widget=forms.TextInput(
    attrs={
      'class': 'form-control bg-light'
    }
  ))

  last_name = forms.CharField(label="Last name required", widget=forms.TextInput(
    attrs={
      'class': 'form-control bg-light'
    }
  ))

  email = forms.EmailField(label="Email required", widget=forms.EmailInput(
    attrs={
      'class': 'form-control bg-light'
    }
  ))

  password = forms.CharField(label="Password required", widget=forms.PasswordInput(
    attrs={
      'class': 'form-control bg-light'
    }
  ))


  class Meta:
    model = User                                                                                                                                                                      
    fields = ['username', 'first_name', 'last_name', 'email', 'password',]