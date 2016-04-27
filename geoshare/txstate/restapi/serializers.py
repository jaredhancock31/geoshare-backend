#!/usr/bin/env python
from rest_framework import serializers
from .models import Droplet
from django.contrib.auth import get_user_model


class DropletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Droplet
        fields = ('drop_id', 'owner', 'latitude', 'longitude', 'data')


class UserSerializer(serializers.ModelSerializer):

    droplets = DropletSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'droplets')




