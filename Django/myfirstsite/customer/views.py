from django.shortcuts import render
from django.http import HttpResponse


def name(request):
    return HttpResponse("This is name")

def id(request):
    return HttpResponse("This is id")


# Create your views here.
