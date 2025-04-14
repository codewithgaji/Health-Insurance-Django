from django.urls import path
from .import views

urlpatterns = [
  path('hospitalsdata/', views.getHospital, name= 'AllHospital' )

  # path will take 3 parameters
  # path name - view name - url name
]
