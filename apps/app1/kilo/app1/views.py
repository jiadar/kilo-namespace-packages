from django.http import HttpResponse
from kilo.subpackage1 import functions


def index(request):
    v = functions.fn()
    return HttpResponse(f"app1 index calculation is {v}")
