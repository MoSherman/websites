from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    #Examples:
    # url(r'^$', 'moriahshermancom.views.home', name='home'),
    url(r'^bmm/', include('bmm.urls')),
    url(r'^cv/', include('cv.urls')),
	
    url(r'^admin/', include(admin.site.urls)),
)
