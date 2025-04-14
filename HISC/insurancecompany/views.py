from django.shortcuts import render
from .models import company

# Create your views here.

def getCompanyData(request):
    all_company_data = company.objects.all()                                                                                                                                                    

    context = {
        "all_company_data_key": all_company_data
    }

    return render(request, "company/insurance_company.html", context)