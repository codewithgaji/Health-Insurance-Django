from django.shortcuts import render
from .models import Hospital

# Create your views here.

# I am going to write django-view (function-based)
# To pull all data from hospital table

def getHospital(request):
    # Model-query-- get the data from the model
    all_hospitals = Hospital.objects.all() # select * from hospital_hospital
    return render(request, 'hospitals.html', {"all_hospitals_key": all_hospitals})


