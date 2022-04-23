from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')

def factorial(request, num):
    def fact(n):
        if n == 0:
            return 1
        else:
            return n * fact(n-1)
    return HttpResponse(json.dumps({'factorial of ' +  str(num) + " is " : fact(num)}))