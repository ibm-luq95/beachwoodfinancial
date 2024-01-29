from django.http import HttpResponse
from django.shortcuts import redirect, render


def error_404(request, exception):
    return render(request, "core/errors/404.html", status=404)
