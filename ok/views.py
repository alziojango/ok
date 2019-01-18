from django.http import HttpResponse


def index(request):
    return HttpResponse("ALZIO www.alzio.co.kr")