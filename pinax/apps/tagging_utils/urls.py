from django.conf.urls.defaults import *



urlpatterns = patterns("",
    url(r"^autocomplete/(?P<app_label>\w+)/(?P<model>\w+)/$", "pinax.apps.tagging_utils.views.autocomplete", name="tagging_utils_autocomplete"),
)
