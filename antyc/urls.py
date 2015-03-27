from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',  # Interpret urls as strings
    url(r'^admin/', include(admin.site.urls)),
)
