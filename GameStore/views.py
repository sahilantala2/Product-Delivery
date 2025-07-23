from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
# Create your views here.


def home(request):

    return render(request,'index.html')

def products(request):

    return render(request,'product.html')

def customer(request):

    return render(request,'customer.html')