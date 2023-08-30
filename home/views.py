from django.shortcuts import render
from Images import *
from django.http import HttpResponse

# Create your views here.

def ImageView(request):
    return HttpResponse("Dont have images your device or 404 Error <h1>404 Not Found</h1>")