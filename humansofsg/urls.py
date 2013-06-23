from django.conf import settings
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

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
)

urlpatterns += patterns('',
    (r'^media/(.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),
)