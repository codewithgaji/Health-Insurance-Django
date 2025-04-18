from django.shortcuts import render
from .forms import Signup

# Create your views here.

def signupview(request):
  if request.method == 'POST':
    signform = Signup(request.POST)
    if signform.is_valid():
      signform.save()
      
  else:
     form = signform()

  context = {
    'signform_key': signform
  }

  return render(request, 'users/registration.html', context)