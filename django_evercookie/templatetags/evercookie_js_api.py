from __future__ import unicode_literals
from django import template
from django.utils.html import format_html, mark_safe
from django_evercookie.config import settings

register = template.Library()

"""Set evercookie"""


@register.simple_tag
def set_evercookie(ec_obj, name, value=None):
    """
    Creates an escaped script with the passed arguments and renders
    them into the templates through the template tag.
    :param ec_obj: The name of the JS-objects you want to create.
    :param name: The name of the cookie you want to set.
    :param value: The value (mostly a unique key) for the cookie.
    :return:
    """
    script = "var {ec_obj}=new evercookie();{ec_obj}.set('{name}', '{value}');".format(
        ec_obj=ec_obj,
        name=name,
        value=value or settings.cookie_value
    )
    return format_html(
        "<script>{script}</script>",
        script=mark_safe(script)
    )


"""Cookies will be re-initiated with best candidate"""


@register.simple_tag
def reactivate_evercookie(ec_obj, name):
    context_dict = {"ec_obj": ec_obj, "name": name}

    script = """
        var %(ec_obj)s=new evercookie();
        function getC(dont) {
            %(ec_obj)s.get("%(name)s", function(best, all) {
                for (var item in all)
                     var payload = JSON.stringify({item: all});
            if (!dont)
                getC(1);
        }, dont);
    }
    setTimeout(getC, 300);
    """ % context_dict
    return format_html(
        "<script>{script}</script>",
        script=mark_safe(script)
    )


"""Cookies won't be not re-setted"""


@register.simple_tag
def rediscover_evercookie(ec_obj, name):
    context_dict = {"ec_obj": ec_obj, "name": name}

    script = """
        var %(ec_obj)s=new evercookie();
        function getC(dont) {
            %(ec_obj)s.get("%(name)s", function(best, all) {
                for (var item in all)
                     var payload = JSON.stringify({item: all});
            if (!dont)
                getC(1);
        }, dont);
    }
    setTimeout(getC, 300, 1);
    """ % context_dict
    return format_html(
        "<script>{script}</script>",
        script=mark_safe(script)
    )
