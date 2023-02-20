from django.http import HttpResponse
from kilo.subpackage1 import functions
from kilo.subpackage2 import morefunctions


def index(request):
    v = functions.fn()
    v2 = morefunctions.cfn()
    return HttpResponse(f"app1 index calculation is {v} and {v2}")
