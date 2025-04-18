from django.urls import path
from .views import signupview


urlpatterns= [
  path("User_Registration/", signupview, name="signup")
]