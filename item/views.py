from django.shortcuts import render
from .models import Items

# Create your views here.
def detail(request, pk):
    