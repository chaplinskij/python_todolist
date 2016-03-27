from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^', include('project.urls')),
]
