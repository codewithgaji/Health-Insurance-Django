from .import views
from django.urls import path

urlpatterns = [                                                                                                                                     
   path('companies/', views.getCompanyData, name="Insurance_Companies"),
]    
