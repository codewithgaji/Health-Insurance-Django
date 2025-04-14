from django.db import models

# Create your models here.
GENDER_CHOICES = [
    ('M', 'MALE'),
    ('F', 'FEMALE'),
    ('O', 'OTHER')
]


class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    first_name = models.CharField("Patients First Name",max_length= 50, null = True, blank=True) # max_length is compulsory max_length= 50
    last_name = models.CharField("Patient's Last Name",max_length=50)
    slug = models.SlugField(max_length= 50)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices= GENDER_CHOICES, max_length= 10)
    dateofbirth = models.DateField()
    mobile_number = models.CharField("Patients Phone Number",max_length = 11) # There is no 'min_length' in "CharField"
    email = models.EmailField()
    address = models.TextField()
    profile_image = models.ImageField(upload_to= "images/patients/")

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = "Patient Info"
