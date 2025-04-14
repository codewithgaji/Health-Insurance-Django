from django.shortcuts import render
from django.http import HttpResponse
from hospital.models import Hospital
from patient.models import Patient
from django.db.models import Q
from django.db.models import Avg, Max, Min, Sum
from .forms import Contactform
# Create your views here.

# This is the view
def index(request):
    # return HttpResponse("<h1> Hello! welcome to HISC Project <h1/>")
    return render(request, 'index.html')

def all_model_queries(request):
    patient_age_greaterthan35 =  Patient.objects.filter(age__gt=35) # This is to filter the data
    age35query = patient_age_greaterthan35.query # This is used to display the query commands for the inequalitya
    
    # "startswith" is an inbuilt function, just pass the variable
    # patient_fname_lastname = Patient.objects.filter(first_name__startswith="A") | Patient.objects.filter(last_name__startswith="C")
    # f_name_l_name_query = patient_fname_lastname.query

    # I changed the query here so that's why we have Angela Clar'k' and 'J'ohn Doe displaying
    patient_fname_lastname = Patient.objects.filter(Q(first_name__istartswith = 'J') | Q(last_name__iendswith = 'k'))

    # What we are performing here is called "Exclusion"
    patient_fname_exclude_J = Patient.objects.exclude(first_name__startswith = 'D' )
    patient_exclude_query = patient_fname_exclude_J.query

    # Finding Nth records of a query set using the 'order_by' 2nd record/1st record/0 record
    patient_record = Patient.objects.order_by('dateofbirth')[1] # this arranges the records based on thier DOB
    # patient_record_query =  patient_record.query
    

    # Calculating the aggregate of integer column of a data element
    patient_avg_age = Patient.objects.all().aggregate(Avg('age'), Max('age')) # to get the maximu age                                                                                                                                   


    # Getting the Patient Count
    patient_count = Patient.objects.all().count()

    context = {
        "patient_age_greaterthan35_key" : patient_age_greaterthan35,
        "age35query_key": age35query, # To check the SQL query
        "patient_fname_lastname_key": patient_fname_lastname,
        "f_name_l_name_query_key": patient_fname_lastname.query,
        "patient_fname_exclude_J_key" : patient_fname_exclude_J,
        "patient_exclude_query_key": patient_exclude_query,
        "patient_record_key": patient_record,
        "patient_avg_age_key": patient_avg_age,
        "patient_count_key": patient_count,
        #"patient_record_query_key" : patient_record_query,
    }
    return render(request, 'modelQueries.html', context)



def contactView(request):
    if request.method == 'POST': # 'POST' is always in uppercase
        form = Contactform(request.POST)
        if form.is_valid():
            return HttpResponse("Your data is submitted")
        
    else:
        form = Contactform()

    context = {
        'form_key': form
    }
    return render(request, "contact.html", context)       