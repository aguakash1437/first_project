from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def cr7(request):
    return HttpResponse('<h1><marquee>crstiano ronaldo</h1></marquee>')

def pogba(request):
    return HttpResponse('<h1> footballer</h1>')