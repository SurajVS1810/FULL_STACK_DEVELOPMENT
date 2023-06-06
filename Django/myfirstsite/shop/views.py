from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def owner(request):
    return HttpResponse("This is owner")

def client(request):
    return HttpResponse("This is client")

def place(request):
    return HttpResponse("This is place")