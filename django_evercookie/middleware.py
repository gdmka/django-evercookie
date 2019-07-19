from django_dont_vary_on.middleware import RemoveUnneededVaryHeadersMiddleware

from django.utils.deprecation import MiddlewareMixin


class RemoveUnneededVaryHeadersMiddlewareCompat(RemoveUnneededVaryHeadersMiddleware, MiddlewareMixin):
    pass
