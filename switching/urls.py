from django.conf.urls import url, include
from . import views
app_name = 'switching'
urlpatterns =[
    url(r'^$', views.home, name='home'),
    url(r'^info/$', views.test, name='test'),
    url(r'^info/(?P<serverName>[a-z]+)/(?P<characterName>[^ \t\r\n\v\f]+)/$', views.info),
    url(r'^info/[a-z]+/$', views.not_found, name='test'),
]
