from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . forms import *
from django.contrib import messages

# Create your views here.
def donateBloodView(request):
    form = donorForm()
    context = {'form':form}
    if request.method=="POST":
        print("Donate")
        form = donorForm(request.POST)
        age = request.POST['age']
        if int(age) <18 or int(age)>65:
            messages.info(request, "Legal age to donate blood is between 18 and 65")
        elif form.is_valid():
            form.save()
            messages.success(request,"Details sent for verification Successfully")
        
    return render(request, "donateBlood/donor.html",context)