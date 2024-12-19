from django.urls import path
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'html/index.html')
