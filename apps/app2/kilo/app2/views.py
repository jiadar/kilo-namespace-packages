from django.http import HttpResponse


def index(request):
    return HttpResponse("app2 index")
