from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"home.html",{'name':'hari'});

def predict(request):
    return render(request,"predict.html")

def map(request):
    return render(request,"map.html")

def EV_Charging(request):
    return render(request,"EV Charging.html")

def conclusion(request):
    return render(request,"conclusion.html")