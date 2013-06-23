from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', RedirectView.as_view(url='https://www.facebook.com/HumansOfSG')),
    # url(r'^humansofsg/', include('humansofsg.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
