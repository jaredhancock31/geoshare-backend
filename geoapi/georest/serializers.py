#!/usr/bin/env python
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from models import Droplet #, AppUser
from rest_framework import serializers
from rest_framework.authtoken.models import Token

__author__ = 'jared hancock'

class AppUserSerializer(serializers.ModelSerializer):
    """
    Django User model without passwords
    """
    droplets = serializers.PrimaryKeyRelatedField(many=True, queryset=Droplet.objects.all())

    class Meta:
        # model = AppUser
        model = get_user_model()
        fields = ('username', 'email', 'droplets')
        read_only_fields = ('email',)


class DropletSerializer(serializers.ModelSerializer):

    # user_id = UserSerializer()
    # user_id = serializers.Field('User.user_id')
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Droplet
        fields = ('drop_id', 'owner', 'latitude', 'longitude', 'data', 'timestamp')

