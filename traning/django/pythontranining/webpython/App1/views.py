from django.shortcuts import render
from django.http import HttpResponse #return home page

def projects(request,pk):
    return HttpResponse("This is my first application"+' '+str(pk))

def HomePage(request):
    return HttpResponse("This Is My first website")
# Create your views here.
