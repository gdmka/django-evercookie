Django Evercookie
=================

Django Evercookie is an implementation of [Evercookie] (http://en.wikipedia.org/wiki/Evercookie) with Django backend services.
Evecrookie core component was rebuilt to use of Django's batteries, so all configurations and hook-ups are done in plain Python and Django's templatetags.

Note: Django 1.5 or later required.

Contributions
-----------------
The project hasn't been maintained for quite some time.
Afaik later Django versions have some API changes that require the backend to be modified.
If you want to contribute to the project and keep it up to date, please send pull requests.


Browser Storage Mechanisms Supported in Django Evercookie
---------------------------------------------------------

Client browsers must support as many of the following storage mechanisms as
possible in order for Evercookie to be effective.

- Standard [HTTP Cookies](http://en.wikipedia.org/wiki/HTTP_cookie)
- Flash [Local Shared Objects](http://en.wikipedia.org/wiki/Local_Shared_Object)
- CSS [History Knocking](http://samy.pl/csshack/)
- Storing cookies in [HTTP ETags](http://en.wikipedia.org/wiki/HTTP_ETag)
- Storing cookies in [Web cache](http://en.wikipedia.org/wiki/Web_cache)
- [window.name caching](http://en.wikipedia.org/wiki/HTTP_cookie#window.name)
- Internet Explorer [userData storage](http://msdn.microsoft.com/en-us/library/ms531424.aspx)
- HTML5 [Session Storage](http://dev.w3.org/html5/webstorage/#the-sessionstorage-attribute)
- HTML5 [Local Storage](http://dev.w3.org/html5/webstorage/#dom-localstorage)
- HTML5 [Global Storage](https://developer.mozilla.org/en/dom/storage#globalStorage)
- HTML5 [Database Storage via SQLite](http://dev.w3.org/html5/webdatabase/)
- HTML5 Canvas - Cookie values stored in RGB data of auto-generated, force-cached PNG images
- HTML5 [IndexedDB](http://www.w3.org/TR/IndexedDB/)


External Dependencies
---------------------

- [Django Don't Vary On] (https://github.com/rory/django-dont-vary-on)

Is used to turn off Vary HTTP headers for some views because Django adds this headers automatically if Auth and Session middlewares are used.

- [Python Imaging Library] (http://www.pythonware.com/products/pil/)

To generate PNG cookies.

Installation
------------
1. Install Python Egg
```
pip install git+https://github.com/gdmka/django_evercookie.git#egg=django-evercookie
```
2. Add Django Evercookie to INSTALLED_APPS
```python
INSTALLED_APPS += ('django_evercookie',)
```
3. Add RemoveUnneededVaryHeadersMiddleware at the top of MIDDLEWARE_CLASSES in settings.py:
```python
MIDDLEWARE_CLASSES = (
    'django_evercookie.middleware.RemoveUnneededVaryHeadersMiddlewareCompat',
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
    )
```
4. Add routing in urls.py
```python
urlpatterns += url('', include((evercookie_urls, 'django_evercookie'))),
```

Basic Configuration
-------------------

Sometimes you need to configure things your way.
Some snippets of configuring Django Evercookie.

```python
from django_evercookie.config import settings
#Changing cookie names for Etag storage
settings.etag_cookie_name = 'etagstorage'
#Enabling CSS History Knocking
settings.history = 'true'
#Setting Django's STATIC_URL manually
settings.static_url = '/cdn/'
```

Using Templatetags
------------------

Add this code to load evercookie in template and set a value.

```html
{% load staticfiles %}
<script src="{% static 'django_evercookie/swfobject-2.2.min.js' %}"></script>
<script src="{% url 'django_evercookie.views.evercookie_core' %}"></script>
{% load evercookie_js_api %}
{% set_evercookie ec_obj='evercookie' name='dummy' value='some_value' %}
```
This will load evercookie core library and render set method.

```javascript
<script>
var evercookie=new evercookie();
evercookie.set("dummy", "some_value");
</script>
```
The get method is as simple as adding
```html
{% rediscover_evercookie ec_obj='evercookie' name='dummy' %}
```
to discover what was set in previous snippet.

Acknowledgement
---------------
Evercookie was developed by [Samy Kamkar](https://github.com/samyk/evercookie), with [contributions from others](https://github.com/samyk/evercookie/graphs/contributors)

License
-------
MIT




