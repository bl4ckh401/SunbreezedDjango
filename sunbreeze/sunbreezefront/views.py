from django.http import request
from django.shortcuts import render

def index(request, *args, **kwargs):
    return render(request, './index.html')