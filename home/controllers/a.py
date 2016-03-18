from django.http import *


def index(request):
    return HttpResponse(u"出来吧！马化腾")