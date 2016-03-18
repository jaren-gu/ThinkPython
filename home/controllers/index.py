from django.http import *


def index(request):
    return HttpResponse(u"就决定是你了！马化腾")