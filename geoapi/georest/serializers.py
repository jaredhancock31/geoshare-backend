from django.contrib.auth.models import User
from models import Droplet #, AppUser
from rest_framework import serializers


class AppUserSerializer(serializers.ModelSerializer):
    """
    This class will serialize User instances in the database into JSON format
    """
    droplets = serializers.PrimaryKeyRelatedField(many=True, queryset=Droplet.objects.all())

    class Meta:
        # model = AppUser
        model = User
        fields = ('id', 'username', 'email', 'droplets')
    #     write_only_fields = ('password',)
    #     read_only_fields = ('id', 'is_staff', 'is_superuser', 'is_active', 'date_joined',)
    #


class DropletSerializer(serializers.ModelSerializer):

    # user_id = UserSerializer()
    # user_id = serializers.Field('User.user_id')
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Droplet
        fields = ('drop_id', 'owner', 'latitude', 'longitude', 'data', 'timestamp')

