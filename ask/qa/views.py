from django.http import HttpResponse


def ok_page(request, *args, **kwargs):
    return HttpResponse('OKay')