from django.http import HttpResponse
from django.shortcuts import redirect, render


def error_500(request):
    return render(request, "core/errors/500.html", status=500)
