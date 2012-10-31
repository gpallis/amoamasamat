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
    url(r'^signin/$', 'webpages.views.signin'),
    url(r'^signout/$', 'webpages.views.signout'),
    
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url':'static/favicon.ico'}),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
