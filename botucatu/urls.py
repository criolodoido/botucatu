from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^petmania/', include('pet.urls', namespace='petmania')),
    url(r'^mozix/', include('mozi.urls', namespace='mozix')),
]
