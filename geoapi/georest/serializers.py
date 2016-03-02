# from django.contrib.auth.models import User
from models import User, Droplet
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    This class will serialize User instances in the database into JSON format
    """

    class Meta:
        model = User
        fields = ('user_id', 'name', 'surname', 'email')


class DropletSerializer(serializers.ModelSerializer):

    user_id = UserSerializer()

    class Meta:
        model = Droplet
        fields = ('drop_id', 'user_id', 'latitude', 'longitude', 'data', 'timestamp')
