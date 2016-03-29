"""geoapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from georest.views import droplet_query
from georest import views
from rest_framework.urlpatterns import format_suffix_patterns

# TODO separate urls and use include import
urlpatterns = [
    # url(r'^user/$', views.UserList.as_view()),
    # url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^droplet/$', views.DropletList.as_view()),
    url(r'^droplet/(?P<pk>[0-9]+)/$', views.DropletDetail.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    # url(r'^user/$', user_list, name='user_list'),
    # url(r'^user/(?P<pk>[0-9]+)/$', user_detail, name='user_detail'),
    # url(r'^droplet/$', droplet_list, name='droplet_list'),
    # url(r'^droplet/(?P<pk>[0-9]+)/$', droplet_detail, name='droplet_detail'),
    # url(r'^droplet/(?P<latitude>-?\d+(?:\.\d+)?P<longitude>-?\d+(?:\.\d+))/$', droplet_query, name='droplet_query'),
    # url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api/', include(router.urls)),

]


urlpatterns = format_suffix_patterns(urlpatterns)
