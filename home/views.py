from django.shortcuts import render
from django.http import *
from home.controller import a

# Create your views here.
def index(request):
    return a.index(request)

def other(request):
    return HttpResponse(u"home/other")