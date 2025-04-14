from django.contrib import admin
from .models import Claim, ClaimStatus

# Register your models here.

admin.site.register(Claim)
admin.site.register(ClaimStatus)