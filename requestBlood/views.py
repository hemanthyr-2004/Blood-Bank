from os import linesep
from django import http
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import*
from donateBlood.models import *
import random
# Generating a pdf
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



def apositive(request):
    disp = []
    data = donor.objects.all()
    for obj in data:
        if obj.BloodType == 'a+' and obj.verify==True:
            disp.append(obj)
    
    if request.method=="POST":
        obj = random.choice(disp)
        Receiver.objects.create(Receiver_Name=request.user, Donor_Name=obj.Name, Donor_Phone=obj.Phone) 
        buf = io.BytesIO()
        # create a  canvas
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        # create a text object
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Helvetica",14)

        heading = "Thank you for using our portal. This is your appointment report"
        line1 = "Receiver name : " + str(request.user)
        line2 = "Donor name : " + str(obj.Name)
        line3 = "Donor Phone : " + str(obj.Phone)
        # Adding lines of text
        lines = [
            heading,
            line1,
            line2,
            line3
        ]

        for line in lines:
            textob.textLine(line)

        obj.delete()
        # finish up
        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename='report.pdf')
        
    context={'data':disp}
    print(disp)
    return render(request, "requestBlood/apos.html", context)

def bpositive(request):
    disp = []
    data = donor.objects.all()
    for obj in data:
        if obj.BloodType == 'b+' and obj.verify==True:
            disp.append(obj)
    # print(disp)

    if request.method=="POST":
        obj = random.choice(disp)
        Receiver.objects.create(Receiver_Name=request.user, Donor_Name=obj.Name, Donor_Phone=obj.Phone) 
        buf = io.BytesIO()
        # create a  canvas
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        # create a text object
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Helvetica",14)

        heading = "Thank you for using our portal. This is your appointment report"
        line1 = "Receiver name : " + str(request.user)
        line2 = "Donor name : " + str(obj.Name)
        line3 = "Donor Phone : " + str(obj.Phone)
        # Adding lines of text
        lines = [
            heading,
            line1,
            line2,
            line3
        ]

        for line in lines:
            textob.textLine(line)

        obj.delete()
        # finish up
        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename='report.pdf')
        
    context={'data':disp}
    return render(request, "requestBlood/bpos.html", context)

def opositive(request):
    disp = []
    data = donor.objects.all()
    for obj in data:
        if obj.BloodType == 'o+' and obj.verify==True:
            disp.append(obj)
    # print(disp)

    if request.method=="POST":
        obj = random.choice(disp)
        Receiver.objects.create(Receiver_Name=request.user, Donor_Name=obj.Name, Donor_Phone=obj.Phone) 
        buf = io.BytesIO()
        # create a  canvas
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        # create a text object
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Helvetica",14)

        heading = "Thank you for using our portal. This is your appointment report"
        line1 = "Receiver name : " + str(request.user)
        line2 = "Donor name : " + str(obj.Name)
        line3 = "Donor Phone : " + str(obj.Phone)
        # Adding lines of text
        lines = [
            heading,
            line1,
            line2,
            line3
        ]

        for line in lines:
            textob.textLine(line)

        obj.delete()
        # finish up
        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename='report.pdf')
        
    context={'data':disp}

   
        
        
    return render(request, "requestBlood/opos.html", context)


def abpositive(request):
    disp = []
    data = donor.objects.all()
    for obj in data:
        if obj.BloodType == 'ab+' and obj.verify==True:
            disp.append(obj)
    # print(disp)

    if request.method=="POST":
        obj = random.choice(disp)
        Receiver.objects.create(Receiver_Name=request.user, Donor_Name=obj.Name, Donor_Phone=obj.Phone) 
        buf = io.BytesIO()
        # create a  canvas
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        # create a text object
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Helvetica",14)

        heading = "Thank you for using our portal. This is your appointment report"
        line1 = "Receiver name : " + str(request.user)
        line2 = "Donor name : " + str(obj.Name)
        line3 = "Donor Phone : " + str(obj.Phone)
        # Adding lines of text
        lines = [
            heading,
            line1,
            line2,
            line3
        ]

        for line in lines:
            textob.textLine(line)

        obj.delete()
        # finish up
        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename='report.pdf')
        
    context={'data':disp}
    return render(request, "requestBlood/abpos.html", context)


def anegative(request):
    disp = []
    data = donor.objects.all()
    for obj in data:
        if obj.BloodType == 'a-' and obj.verify==True:
            disp.append(obj)
    # print(disp)

    if request.method=="POST":
        obj = random.choice(disp)
        Receiver.objects.create(Receiver_Name=request.user, Donor_Name=obj.Name, Donor_Phone=obj.Phone) 
        buf = io.BytesIO()
        # create a  canvas
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        # create a text object
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Helvetica",14)

        heading = "Thank you for using our portal. This is your appointment report"
        line1 = "Receiver name : " + str(request.user)
        line2 = "Donor name : " + str(obj.Name)
        line3 = "Donor Phone : " + str(obj.Phone)
        # Adding lines of text
        lines = [
            heading,
            line1,
            line2,
            line3
        ]

        for line in lines:
            textob.textLine(line)

        obj.delete()
        # finish up
        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename='report.pdf')
        
    context={'data':disp}
    return render(request, "requestBlood/aneg.html", context)

def bnegative(request):
    disp = []
    data = donor.objects.all()
    for obj in data:
        if obj.BloodType == 'b-' and obj.verify==True:
            disp.append(obj)
    # print(disp)

    if request.method=="POST":
        obj = random.choice(disp)
        Receiver.objects.create(Receiver_Name=request.user, Donor_Name=obj.Name, Donor_Phone=obj.Phone) 
        buf = io.BytesIO()
        # create a  canvas
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        # create a text object
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Helvetica",14)

        heading = "Thank you for using our portal. This is your appointment report"
        line1 = "Receiver name : " + str(request.user)
        line2 = "Donor name : " + str(obj.Name)
        line3 = "Donor Phone : " + str(obj.Phone)
        # Adding lines of text
        lines = [
            heading,
            line1,
            line2,
            line3
        ]

        for line in lines:
            textob.textLine(line)

        obj.delete()
        # finish up
        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename='report.pdf')
        
    context={'data':disp}
    return render(request, "requestBlood/bneg.html", context)

def onegative(request):
    disp = []
    data = donor.objects.all()
    for obj in data:
        if obj.BloodType == 'o-' and obj.verify==True:
            disp.append(obj)

    if request.method=="POST":
        obj = random.choice(disp)
        Receiver.objects.create(Receiver_Name=request.user, Donor_Name=obj.Name, Donor_Phone=obj.Phone) 
        buf = io.BytesIO()
        # create a  canvas
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        # create a text object
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Helvetica",14)

        heading = "Thank you for using our portal. This is your appointment report"
        line1 = "Receiver name : " + str(request.user)
        line2 = "Donor name : " + str(obj.Name)
        line3 = "Donor Phone : " + str(obj.Phone)
        # Adding lines of text
        lines = [
            heading,
            line1,
            line2,
            line3
        ]

        for line in lines:
            textob.textLine(line)

        obj.delete()
        # finish up
        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename='report.pdf')
        
        
    context={'data':disp}
    return render(request, "requestBlood/oneg.html", context)

def abnegative(request):
    disp = []
    data = donor.objects.all()
    for obj in data:
        if obj.BloodType == 'ab-' and obj.verify==True:
            disp.append(obj)
    # print(disp)

    if request.method=="POST":
        obj = random.choice(disp)
        Receiver.objects.create(Receiver_Name=request.user, Donor_Name=obj.Name, Donor_Phone=obj.Phone) 
        buf = io.BytesIO()
        # create a  canvas
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        # create a text object
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Helvetica",14)

        heading = "Thank you for using our portal. This is your appointment report"
        line1 = "Receiver name : " + str(request.user)
        line2 = "Donor name : " + str(obj.Name)
        line3 = "Donor Phone : " + str(obj.Phone)
        # Adding lines of text
        lines = [
            heading,
            line1,
            line2,
            line3
        ]

        for line in lines:
            textob.textLine(line)

        obj.delete()
        # finish up
        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename='report.pdf')
        
    context={'data':disp}
    return render(request, "requestBlood/abneg.html", context)



@login_required(login_url='login')
def display(request):
    
    data = donor.objects.all()
    count_ap=0
    count_op=0
    count_bp=0
    count_an=0
    count_bn=0
    count_on=0
    count_abp=0
    count_abn=0

    for obj in data:
        if obj.BloodType == "a+" and obj.verify==True:
            count_ap+=1
        elif obj.BloodType =="b+" and obj.verify==True:
            count_bp+=1
        elif obj.BloodType =="o+" and obj.verify==True:
            count_op+=1
        elif obj.BloodType =="a-" and obj.verify==True:
            count_an+=1
        elif obj.BloodType =="b-" and obj.verify==True:
            count_bn+=1
        elif obj.BloodType =="o-" and obj.verify==True:
            count_on+=1
        elif obj.BloodType =="ab+" and obj.verify==True:
            count_abp+=1
        elif obj.BloodType =="ab-" and obj.verify==True:
            count_abn+=1

    context = {'donor':data, 'c_ap':count_ap, 'c_bp':count_bp,'c_op':count_op,'c_an':count_an,'c_bn':count_bn,'c_on':count_on,'c_abp':count_abp,'c_abn':count_abn}
    return render(request,'requestBlood/index.html',context)

def loginView(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password = password )
        
        if user:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,"Invalid username or password")
            return render(request,'requestBlood/login.html')

    return render(request,'requestBlood/login.html')

def register(request):
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account was created successfully")
            return redirect('login')


    context = {'form':form}
    return render(request,'requestBlood/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')