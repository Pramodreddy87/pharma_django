import os
from django.conf.urls import patterns, include, url
from blog.views import index
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
SITE_ROOT=SITE_ROOT[:-6]+'\\'+'static_media'
urlpatterns = patterns('',
    # Examples:
    url(r'^$',index),

    # url(r'^Pharma/', include('Pharma.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('django.views.static',
    (r'^static_media/(?P<path>.*)$',
     'serve', {
        'document_root':SITE_ROOT,
        'show_indexes': True }),)