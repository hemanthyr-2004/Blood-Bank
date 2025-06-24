from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class donor(models.Model):
    Name = models.CharField(max_length=200)
    Phone = models.CharField(max_length=10)
    Email = models.EmailField(max_length=200, null=True, blank=True)
    Address = models.CharField(max_length=350)
    blood_types = (
        ('a+', 'A+'),
        ('b+', 'B+'),
        ('o+', 'O+'),
        ('ab+', 'AB+'),
        ('a-', 'A-'),
        ('b-', 'B-'),
        ('o-', 'O-'),
        ('ab-', 'AB-'),
    )
    BloodType = models.CharField(max_length=9, choices=blood_types)
    
    age = models.IntegerField(
         validators=[MaxValueValidator(65), MinValueValidator(18)]
    )

    medical_ailments = models.CharField(max_length=500, null=True,blank=True)

    verify = models.BooleanField( null=True,blank=True)

    def __str__(self):
        return self.Name
    
