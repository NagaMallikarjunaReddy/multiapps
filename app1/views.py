from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app1f1(request):
    return HttpResponse('<h1>This is the 1st view of app1</h1>')

def app1f2(request):
    return HttpResponse('<h1>This is the 2nd view of app1</h1>')