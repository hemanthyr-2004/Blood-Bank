from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import *

class donorForm(ModelForm):
       
    # def clean_age(self):
    #     data= self.cleaned_data.get("age")
    #     if data>65 or data<18:
    #         # raise ValidationError("Age must be between 18 and 65")
    #         raise forms.ValidationError("error")
    #         print("errorroror")
    #     return data

    class Meta:
        model = donor
        fields = ['Name','Phone','Email','Address','BloodType', 'age','medical_ailments']
    
    # def clean_age(self):
    #     age= self.cleaned_data.get("age")
    #     if age < 18:
    #         raise ValidationError("You must be at least 18 years old to donate")
    #     return age
