from django.contrib import admin
from geoapi.georest.models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass


class DropletAdmin(admin.DropletAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Droplet, DropletAdmin)
