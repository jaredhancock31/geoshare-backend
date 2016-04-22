#!/usr/bin/env python
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from models import Droplet
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Django User model with a one-to-many relation to Droplets
    """
    # droplets = serializers.PrimaryKeyRelatedField(many=True, queryset=Droplet.objects.all())
    droplets = DropletSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'droplets')
        # model = get_user_model()  # Django User model
        # read_only_fields = ('email',)
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)


class DropletSerializer(serializers.ModelSerializer):

    # user_id = UserSerializer()
    # user_id = serializers.Field('User.user_id')
    # owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Droplet
        fields = ('drop_id', 'owner', 'latitude', 'longitude', 'data', 'timestamp')

