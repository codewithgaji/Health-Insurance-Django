from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('all_queries', views.all_model_queries, name = "AllQueries"),
    path("forms/", views.contactView, name= "contact")                                                                                                                  
    # --('url path', view-func, url name)
]
