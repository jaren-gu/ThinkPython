from django.http import *

def index(request):
    return HttpResponse(u"home/index")