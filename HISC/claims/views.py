from django.shortcuts import render
from .models import Claim

# Create your views here.

def get_all_claims(request):

    all_claims = Claim.objects.all()

    context = {
        "all_claims_key": all_claims
    }
                                                                                                                                                                                
    return render(request, "Claims/all_claims.html", context)




