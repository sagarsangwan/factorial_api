from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')

def factorial(request, num):
    try:
        num = int(num)
    except ValueError:
        return HttpResponse('Please enter a number.')
    if num < 0:
            return HttpResponse('Please enter a positive number.')

    def fact(num):
        
        
        if num == 0:
            return 1
        else:
            return num * fact(num-1)
    return JsonResponse({'factorial': fact(int(num))})