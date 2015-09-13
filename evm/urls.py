from django.conf.urls import include, url
from django.contrib import admin
import events, attendees

urlpatterns = [
    # Examples:
    url(r'^$', 'evm.views.home', name='home'),
    url(r'^events/', include('events.urls')),
    url(r'^attendees/', include('attendees.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
