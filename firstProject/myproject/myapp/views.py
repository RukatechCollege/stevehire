from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home (request):
    return HttpResponse("<h1> Welcome to Django </h1> ")

def about (request):
    return HttpResponse("Welcome to About us")

def contact (request):
    return HttpResponse("This is my Contact us Page")

