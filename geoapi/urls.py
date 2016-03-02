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
from django.conf.urls import url
from django.contrib import admin
from georest.views import user_list, user_detail, droplet_list, droplet_detail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^user/$', user_list, name='user_list'),
    url(r'^user/(?P<pk>[0-9]+)/$', user_detail, name='user_detail'),
    url(r'^droplet/$', droplet_list, name='droplet_list'),
    url(r'^droplet/(?P<pk>[0-9]+)/$', droplet_detail, name='droplet_detail'),
    url(r'^admin/', admin.site.urls),
]


urlpatterns = format_suffix_patterns(urlpatterns)
