from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'src.views.home', name='home'),
                       # url(r'^src/', include('src.foo.urls')),
                       
                       url(r'^$', include('apps.bottomlessPit.urls')),
                       url(r'^test', include('apps.bottomlessPit.urls')),
                       
                       url(r'^grappelli/', include('grappelli.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )

baseurlregex = r'^media/(?P<path>.*)$'
if settings.SERVE_STATIC == True :
    urlpatterns = urlpatterns+patterns('',
                                       (baseurlregex, 'django.views.static.serve',
                                        {'document_root':  settings.MEDIA_ROOT,'show_indexes': True}),
                                       )
    
    urlpatterns = urlpatterns + patterns('',(url(r'^twango_dashboard/',include('twango.twango_dashboard.urls'))),) 
    
urlpatterns = urlpatterns + patterns('',(url(r'^.*$',include('src.apps.bottomlessPit.urls'))),) 
