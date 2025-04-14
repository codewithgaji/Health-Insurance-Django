from django.db import models

# Create your models here.

class company(models.Model):
    insurance_company_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    details = models.TextField()                                                                                                            
    image = models.ImageField(upload_to= "images/companies/", default="Not specified")

    def __str__(self):
        return self.name