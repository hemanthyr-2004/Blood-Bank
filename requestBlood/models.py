from django.db import models

# Create your models here.

class Receiver(models.Model):
    Receiver_Name = models.CharField(max_length=200)
    Donor_Name = models.CharField(max_length=200)
    Donor_Phone = models.CharField(max_length=10)

    def __str__(self) :
        return self.Receiver_Name
