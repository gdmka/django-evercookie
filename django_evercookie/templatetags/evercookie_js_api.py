from django import template
from django_evercookie.config import settings
register = template.Library()


"""Set evercookie"""
@register.simple_tag
def set_evercookie(ec_obj, name, value=None):
    if value is None:
        context_dict = {"ec_obj": ec_obj, "name": name, "value": settings.cookie_value}
    else:
        context_dict = {"ec_obj": ec_obj, "name": name, "value": value}

    return '''<script>
var %(ec_obj)s=new evercookie();
%(ec_obj)s.set("%(name)s", "%(value)s");
</script>''' % context_dict


"""Cookies will be re-setted with best candidate"""
@register.simple_tag
def reactivate_evercookie(ec_obj, name):
    context_dict = {"ec_obj": ec_obj, "name": name}

    return '''<script>
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
</script>''' % context_dict


"""Cookies won't be not re-setted"""
@register.simple_tag
def rediscover_evercookie(ec_obj, name):
    context_dict = {"ec_obj": ec_obj, "name": name}

    return '''<script>
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
</script>''' % context_dict
