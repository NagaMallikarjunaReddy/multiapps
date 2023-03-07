from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2f1(request):
    return HttpResponse('<h2>This is 1st view of app2</h2>')

def app2f2(request):
    return HttpResponse('<h2>This is the 2nd view of app2</h2>')