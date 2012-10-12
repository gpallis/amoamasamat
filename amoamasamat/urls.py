from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'webpages.views.home', name='home'),
    
    url(r'^lessons/$', 'webpages.views.showLearningPage', {'pageLevelString':'1.00'}), #if no param, goto lesson 0. This pattern is used as the base URL for links in the template.
    url(r'^lessons/(?P<pageLevelString>\d\.\d+)/$', 'webpages.views.showLearningPage'),
    url(r'^play/$', 'webpages.views.play'),
    url(r'^signup/$', 'webpages.views.showSignUpPage'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
