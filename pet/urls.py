from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.petmania, name='petmania'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='detalhe'),
	url(r'^comida$', views.comida, name='comida'),
	url(r'^educacao$', views.educacao, name='educacao'),
	url(r'^acessorios$', views.acessorios, name='acessorios'),
	url(r'^higienizacao$', views.higiene, name='higiene'),
	]