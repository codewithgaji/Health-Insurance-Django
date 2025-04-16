from django import forms
from .models import ContactM
# THIS IS A DJANGO-PYTHON  CLASS
class Contactform(forms.Form): # This is a python class
  name  = forms.CharField(max_length=30) # Foreign Key does not exist in forms.py
  email = forms.EmailField()
  mobile = forms.IntegerField() # Positive integer field does not exist here                                                                                                                                          


class ContactModelForm(forms.ModelForm):
  class Meta:
    model = ContactM # To avoid Creating the fields over again
    fields = '__all__' # or ['name', 'email'] you decide the fields you want to display                                                                                                                 

