from django.db import models
from datetime import datetime

# Create your models here.
# using inheritance method

# Foreign Key table
class Hospital_type(models.Model):
    type_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.type_name # This ensures the dropdown shows readable names



class Hospital(models.Model):
    hospital_id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Hospital_type, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length=50) # this is a URL friendly version of a string
    address = models.TextField()
    updated_date = models.DateTimeField(default=datetime.now)
    logo = models.ImageField(upload_to="images/hospital/", blank = True, null=True)

    def __str__(self):
        return self.name # This ensures the dropdown shows readable names

# Table name = app name_Django Model-name
# ! -----------hospital_Hospital ---> hospital_Hospital

