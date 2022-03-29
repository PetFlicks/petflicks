from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')# send user to the templates html page cw

def topic(request):
    return render(request, 'topic.html')# send user to the templates html page cw