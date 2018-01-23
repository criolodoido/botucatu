from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^vital/$', views.vital, name='vital'),
	url(r'^bairro/$', views.bairro, name='bairro'),
	url(r'^centro/$', views.centro, name='centro'),
	url(r'^domlucio/$', views.domlucio, name='domlucio'),
	url(r'^facaparte/$', views.facaparte, name='parte'),
]