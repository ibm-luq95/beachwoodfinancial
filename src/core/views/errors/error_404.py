from django.http import HttpResponse
from django.shortcuts import redirect, render


def error_404(request, exception):
    """
    Render the "core/errors/404.html" template with a status code of 404.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that caused the 404 error.

    Returns:
        HttpResponse: The rendered HTTP response.

    """
    return render(request, "core/errors/404.html", status=404)
