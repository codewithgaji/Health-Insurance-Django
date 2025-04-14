from django import forms

# THIS IS A DJANGO-PYTHON  CLASS
class Contactform(forms.Form): # This is a python class
  name  = forms.CharField(max_length=30) # Foreign Key does not exist in forms.py
  email = forms.EmailField()
  mobile = forms.IntegerField() # Positive integer field does not exist here                                                                                                                                          



