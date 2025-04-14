from django.shortcuts import render
from .models import Patient

# Create your views here.

def getAllPatients(request):
    all_patients = Patient.objects.all().order_by('patient_id')
    return render(request, 'patient/patients.html', {"all_patients_key": all_patients})

def get_patient_info(request, nameslug): # Second parameter from urls.py parameter("<int: patient_id>")
    get_one_patient = Patient.objects.filter(slug = nameslug) # the "field=value" part of filter is to ensure the model name corresponds to whatever dispatcher we provide in the urls.py.
    
    # This is used to select x from patient when patient_id is a dynamic value
    context = {
        "get_one_patient_key": get_one_patient
    }

    return render(request,
                  'patient/patient_details.html', # this is the dir of the html page
                    context # this is the dictionary that we created above
                    )
