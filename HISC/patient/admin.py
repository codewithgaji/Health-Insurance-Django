from django.contrib import admin
from .models import Patient
# Register your models here.


#admin.site.register(Patient)

class PatientAdmin(admin.ModelAdmin):
    # list_display is a predefined functionality
    list_display = ['first_name','last_name', 'age', 'gender', "dateofbirth"]                                                                                                           
    prepopulated_fields = { # This is used to create an automatic 'slug' for the fields chosen
        'slug': ['first_name', 'last_name']
    }

admin.site.register(Patient, PatientAdmin)
