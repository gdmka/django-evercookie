from __future__ import unicode_literals
from functools import wraps

from django.http import HttpResponseNotModified
"""If cookie name was not found in the request server returns 304
Otherwise view logic executes."""


def cookie_exists(cookie_name):
    def render(f):
        @wraps(f)
        def wrapper(request, *args, **kwargs):
            if cookie_name not in request.COOKIES:
                return HttpResponseNotModified()
            return f(request, *args, **kwargs)
        return wrapper
    return render


