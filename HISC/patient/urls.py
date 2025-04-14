from .import views
from django.urls import path

urlpatterns = [
   path('allpatients', views.getAllPatients, name="Patients"),

   # All the path with parameters(<slug:, <str:, <int:) are used for changing url path to whatever we want, either as a string, taking the first/last_name for the url path

   path('patient/<slug:nameslug>/', views.get_patient_info, name="single_patient")
   #path('patient/<str:patient_name>/', views.get_patient_info, name="single_patient")
   #path('patient/<int:patient_id>/', views.get_patient_info, name="single_patient")
]    


