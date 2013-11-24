from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytodo.views.home', name='home'),
    # url(r'^mytodo/', include('mytodo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^todo/$', 'todo.views.index'),
    url(r'^todo/add/$', 'todo.views.add'),
    url(r'^todo/del/(?P<entry_id>\d+)/$', 'todo.views.delete'),
)
