from django.http import *


def index(request):
    return HttpResponse(u"出来吧！马化腾")
    # return HttpResponse(request.GET['a'])