from django.conf.urls import patterns, url
from japan_map import views


urlpatterns = patterns('',
    url(r'^$', views.japan_map, name='japan_map'),
)