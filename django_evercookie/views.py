 #-*- coding: utf-8 -*-

from PIL import Image
from StringIO import StringIO
from copy import deepcopy
from django_dont_vary_on.decorators import dont_vary_on

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from django_evercookie.helpers import cookie_exists
from django_evercookie.config import settings

@dont_vary_on('Cookie', 'Host')
@cookie_exists(settings.cache_cookie_name)
def evercookie_cache(request):

    cookie = request.COOKIES[settings.cache_cookie_name]
    response = HttpResponse(content=cookie, content_type='text/html; charset=UTF-8')
    response['Last-Modified'] = 'Wed, 30 Jun 2010 21:36:48 GMT'
    response['Expires'] = 'Tue, 31 Dec 2030 23:30:45 GMT'
    response['Cache-Control'] = 'private, max-age=630720000'
    response['Content-length'] = len(cookie)

    return response

@dont_vary_on('Cookie', 'Host')
def evercookie_etag(request):

    if settings.etag_cookie_name not in request.COOKIES:
        if 'HTTP_IF_NONE_MATCH' not in request.META:
            response = HttpResponse()
        else:
            response = HttpResponse(content=request.META['HTTP_IF_NONE_MATCH'])
            response['ETag'] = request.META['HTTP_IF_NONE_MATCH']
            response['Content-length'] = len(request.META['HTTP_IF_NONE_MATCH'])

    else:
        response = HttpResponse(content=request.COOKIES[settings.etag_cookie_name], content_type='text/html; charset=UTF-8')
        response['ETag'] = request.COOKIES[settings.etag_cookie_name]
        response['Content-length'] = len(request.COOKIES[settings.etag_cookie_name])

    return response

@cookie_exists(settings.png_cookie_name)
def evercookie_png(request):

    base_img = Image.new('RGB', (200, 1), color=None)
    cookie_value = list(request.COOKIES[settings.png_cookie_name])
    quotient, remainder = divmod(len(cookie_value), 3)
    new_cookie_value = deepcopy(cookie_value)

    #php array returns null when index is out of range
    #ugly python hack simulating that

    if remainder == 1:
        new_cookie_value.extend(['\x00', '\x00'])
    elif remainder == 2:
        new_cookie_value.extend(['\x00'])

    x_axis = 0
    y_axis = 0
    index=0
    buffer = StringIO()

    while index < len(new_cookie_value):
        base_img.putpixel((x_axis, y_axis), (ord(new_cookie_value[index]),
                                           ord(new_cookie_value[index+1]),
                                           ord(new_cookie_value[index+2])))
        index+=3
        x_axis+=1

    base_img.save(buffer, 'PNG')

    response = HttpResponse(content=buffer.getvalue(), content_type="image/png")
    response['Last-Modified'] = 'Wed, 30 Jun 2010 21:36:48 GMT'
    response['Expires'] = 'Tue, 31 Dec 2030 23:30:45 GMT'
    response['Cache-Control'] = 'private, max-age=630720000'

    return response

def evercookie_auth(request):
    """ Boilerplate view  """
    return HttpResponse()

def evercookie_core(request):

    return render_to_response('evercookie.html',
      {'history': settings.history,
        'java': settings.java,
        'tests': settings.tests,
        'silverlight': settings.silverlight,
        'base_url': settings.base_url,
        'png_cookie_name': settings.png_cookie_name,
        'png_path': reverse(settings.png_path),
        'etag_cookie_name': settings.etag_cookie_name,
        'etag_path': reverse(settings.etag_path),
        'cache_cookie_name': settings.cache_cookie_name,
        'cache_path': reverse(settings.cache_path),
        'auth_path': settings.auth_path,
        'domain': settings.domain,
        'static_url': settings.static_url},
         content_type="text/javascript")


