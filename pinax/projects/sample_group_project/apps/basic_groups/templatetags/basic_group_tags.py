from django import template
from basic_groups.forms import BasicGroupForm



register = template.Library()


@register.inclusion_tag("basic_groups/group_item.html")
def show_group(group):
    return {"group": group}


# @@@ should move these next two as they aren't particularly group-specific

@register.simple_tag
def clear_search_url(request):
    getvars = request.GET.copy()
    if "search" in getvars:
        del getvars["search"]
    if len(getvars.keys()) > 0:
        return "%s?%s" % (request.path, getvars.urlencode())
    else:
        return request.path


@register.simple_tag
def persist_getvars(request):
    getvars = request.GET.copy()
    if len(getvars.keys()) > 0:
        return "?%s" % getvars.urlencode()
    return ""
