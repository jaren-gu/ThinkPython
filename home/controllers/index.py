from django.http import *
from django.shortcuts import render


def index(request):
    return render(request, 'home/index/index.html')


def shiwanfute(request):
    return HttpResponse(u"老马已经被电晕")