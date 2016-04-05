#!/usr/bin/env python
from rest_framework import serializers
from .models import Droplet


class DropletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Droplet
        fields = ('drop_id', 'owner', 'latitude', 'longitude', 'data')
