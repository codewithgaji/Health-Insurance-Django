from django.contrib import admin
from .models import Hospital, Hospital_type

# Register your models here.

class Hospital_type_Admin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('type_name',)   
    }

class HospitalAdmin(admin.ModelAdmin):
     prepopulated_fields = {
          'slug': ('name',),
     }
     

admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Hospital_type, Hospital_type_Admin)
