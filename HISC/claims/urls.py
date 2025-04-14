from django.urls import path
from . import views

urlpatterns = [                                                                                                                                             
    path("Claims/", views.get_all_claims, name="All_Claims")
]