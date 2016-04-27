
from django.conf.urls import url, include
from django.contrib import admin
from restapi import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^droplets/all/$', views.DropletList.as_view()),
    url(r'^droplets/q/$', views.DropletQuery.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),


]
