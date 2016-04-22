
from django.conf.urls import url
from django.contrib import admin
from .api import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^droplets/all/$', views.DropletList.as_view()),
    url(r'^droplets/q/$', views.DropletQuery.as_view()),

]
