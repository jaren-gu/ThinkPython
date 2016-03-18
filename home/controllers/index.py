from django.http import *
from django.shortcuts import render


def index(request):
    return render(request, 'home/index/index.html')