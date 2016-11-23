from __future__ import unicode_literals
from django.conf.urls import url
from . import views

"""URLs differ from standart evercookie_<storage_method> to dodge easyprivacy blocking rules"""

urlpatterns = [
    url(r'^ecache/$', views.evercookie_cache, name='evercookie-ecache'),
    url(r'^epng/$', views.evercookie_png, name='evercookie-epng'),
    url(r'^ecetag/$', views.evercookie_etag, name='evercookie-ecetag'),
    url(r'^ecookie/$', views.evercookie_core, name='evercookie-ecookie'),
    url(r'^ecauth/$', views.evercookie_auth, name='evercookie-ecauth'),
]
