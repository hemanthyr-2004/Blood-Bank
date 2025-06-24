from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def UserChoice(request):
    return render(request, "homepage/choice.html")