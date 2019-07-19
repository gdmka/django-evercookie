from django.conf.urls import url

from django_evercookie import views


"""URLs differ from standart evercookie_<storage_method> to dodge easyprivacy blocking rules"""
urlpatterns = [
    url(r'ecache', views.evercookie_cache, name="ecache"),
    url(r'epng', views.evercookie_png, name="epng"),
    url(r'ecetag', views.evercookie_etag, name="ecetag"),
    url(r'ecookie', views.evercookie_core, name="ecookie"),
    url(r'eceauth', views.evercookie_auth, name="eceauth"),
]
