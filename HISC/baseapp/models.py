from django.db import models

# Create your models here.

class ContactM(models.Model):
  name = models.CharField(max_length=50) 
  email = models.EmailField()
  mobile = models.IntegerField()
  message = models.TextField()

  def __str__(self):
    return self.name

