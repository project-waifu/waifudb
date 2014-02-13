from django.conf.urls import patterns, include, url
from Project_WaifuDB.settings import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Project_WaifuDB.views.home', name='home'),
    # url(r'^Project_WaifuDB/', include('Project_WaifuDB.foo.urls')),

    # Project Waifu URLS
    # url(r'^files/', 'Project_WaifuDB.assets.views.imageview'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
# Serve static files in debug.
    urlpatterns += patterns('',
    (r'^files/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT,
    'show_indexes' : True}),
)