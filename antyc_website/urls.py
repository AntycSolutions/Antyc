from django.conf.urls import patterns, include, url
from django.contrib import admin

from antyc import views


urlpatterns = patterns(
    '',  # Interpret urls as strings
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
