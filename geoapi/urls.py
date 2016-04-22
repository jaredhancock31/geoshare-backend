#!/usr/bin/env python
from django.conf.urls import url, include
from django.contrib import admin
from georest import views
from rest_framework.authtoken import views as djangoviews
from rest_framework.urlpatterns import format_suffix_patterns

__author__ = 'jared hancock'


urlpatterns = [

    # url(r'^user/$', views.UserDetail.as_view(), name='rest_user_details'),
    url(r'^droplets/all/$', views.DropletList.as_view()),
    url(r'^droplets/q/$', views.DropletQuery.as_view()),
    url(r'^accounts_api/', include('registration_api.urls')),
    url(r'^register/$', views.UserViewSet.as_view()),
    url(r'^admin/', admin.site.urls),

    # 3rd party views
    # url(r'^auth/', include('rest_auth.urls')),
    # url(r'^auth/registration/', include('rest_auth.registration.urls')),

    # django token auth
    # url(r'^token-auth/', djangoviews.obtain_auth_token),


]


urlpatterns = format_suffix_patterns(urlpatterns)
