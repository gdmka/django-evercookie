from __future__ import unicode_literals
from django.conf import settings
from django.contrib.sites.models import Site

current_site = Site.objects.get_current()


class Meta(type):
    def __init__(cls, *args, **kwargs):
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Meta, cls).__call__(*args, **kwargs)
        return cls.instance


class Settings(object):
    """Django Evercookie Settings Interface"""
    __metaclass__ = Meta

    def __init__(self, etag_cookie_name='etg',
                 etag_path='evercookie-ecetag',
                 png_cookie_name='png',
                 png_path='evercookie-epng',
                 cache_cookie_name='cachec',
                 cache_path='evercookie-ecache',
                 history='false',
                 java='false',
                 silverlight='false',
                 domain='.' + current_site.domain,
                 tests=10,
                 base_url='',
                 auth_path='false',
                 static_url=settings.STATIC_URL + 'django_evercookie/',
                 cookie_value=''):
        self.etag_cookie_name = etag_cookie_name
        self.etag_path = etag_path
        self.png_cookie_name = png_cookie_name
        self.png_path = png_path
        self.cache_cookie_name = cache_cookie_name
        self.cache_path = cache_path
        """  CSS history knocking or not .. can be network intensive """
        self.history = history
        """ Java applet on/off"""
        self.java = java
        """ Silverlight support """
        self.silverlight = silverlight
        self.domain = domain
        """ Max tries to wait / write / read swf, silverlight, png, db and java"""
        self.tests = tests
        """ Base URL for assets, this is Django's STATIC_URL """
        self.base_url = base_url
        self.auth_path = auth_path
        self.static_url = static_url
        self.cookie_value = cookie_value


settings = Settings()
