from django.shortcuts import render
from django.http import *
from home.controller import a

# Create your views here.
def index(request):
    return HttpResponse(u"home/index")


def other(request):
    return HttpResponse(u"home/other")

def other(request, a, b):
    return HttpResponse(u"home/other/%s/%s" %(a,b))