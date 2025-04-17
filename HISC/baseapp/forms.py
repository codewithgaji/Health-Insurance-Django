from django import forms
from .models import ContactM
# THIS IS A DJANGO-PYTHON  CLASS
class Contactform(forms.Form): # This is a python class
  name  = forms.CharField(max_length=30) # Foreign Key does not exist in forms.py
  email = forms.EmailField()
  mobile = forms.IntegerField() # Positive integer field does not exist here                                                                                                                                          


class ContactModelForm(forms.ModelForm):
  name = forms.CharField(label="Enter your name", 
                         help_text= "Kindly input your name in Capital Letter",
                         widget=forms.TextInput(attrs={
                        'class': 'form-control bg-light' # This is a attribute that can have a attribute used to carefully design the forms.
                        
  }))
  email = forms.EmailField(label="Enter your email", widget=forms.EmailInput(attrs={
    'class': 'form-control b-light'
  }))
  mobile = forms.IntegerField(label="Enter you mobile number", widget=forms.TextInput(attrs={
    'class': 'form-control bg-light'
  }))

  message = forms.CharField(label="Your message", widget=forms.Textarea(attrs={
    'class': 'form-control bg-class'
  }))

  
  class Meta:
    model = ContactM # To avoid Creating the fields over again
    fields = '__all__' # or ['name', 'email'] you decide the fields you want to display                                                                                                                 

