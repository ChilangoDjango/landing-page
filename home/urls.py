from django.conf.urls import patterns, url
from home.views import landing

urlpatterns = patterns('',
	url(r'^$', landing.as_view(), name='home'),
)