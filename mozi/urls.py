from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='mozix'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='detalhe'),#mudancas aqui"
	url(r'^doces$', views.doces, name='comida'),
	url(r'^bebidas$', views.bebidas, name='bebidas'),
	url(r'^petiscos$', views.petiscos, name='petiscos'),
	url(r'^salgados$', views.salgados, name='salgados'),
	url(r'^assados$', views.assados, name='assados'),
	]