#!/usr/bin/env python
from django.conf.urls import url, include
from django.contrib import admin
from georest.views import droplet_query
from georest import views
from rest_framework.authtoken import views as djangoviews
from rest_framework.urlpatterns import format_suffix_patterns

__author__ = 'jared hancock'


urlpatterns = [
    # url(r'^user/$', views.UserList.as_view()),
    # url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^user/$', views.UserDetail.as_view(), name='rest_user_details'),
    url(r'^droplet/$', views.DropletList.as_view()),
    # url(r'^droplet/(?P<pk>[0-9]+)/$', views.DropletDetail.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^my-login/$', views.my_login, name='login'),

    # 3rd party views
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),

    # url(r'^user/$', user_list, name='user_list'),
    # url(r'^user/(?P<pk>[0-9]+)/$', user_detail, name='user_detail'),
    # url(r'^droplet/$', droplet_list, name='droplet_list'),
    # url(r'^droplet/(?P<pk>[0-9]+)/$', droplet_detail, name='droplet_detail'),
    # url(r'^droplet/(?P<latitude>-?\d+(?:\.\d+)?P<longitude>-?\d+(?:\.\d+))/$', droplet_query, name='droplet_query'),
    # url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api/', include(router.urls)),
    url(r'^token-auth/', djangoviews.obtain_auth_token),

]


urlpatterns = format_suffix_patterns(urlpatterns)
