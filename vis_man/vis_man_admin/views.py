from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# The log-in page
def login(request):
    return HttpResponse("This is going to be the log-in page.")

# The home page after successful login
def home(request):
    return HttpResponse("This is going to be the home page")
