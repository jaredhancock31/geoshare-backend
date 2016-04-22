#!/usr/bin/env python

from rest_framework.decorators import api_view
from rest_framework.views import APIView, csrf_exempt
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework import permissions
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.http import Http404
from models import Droplet
from django.contrib.auth import get_user_model
from serializers import UserSerializer, DropletSerializer
from permissions import IsOwnerOrReadOnly, IsStaffOrTargetUser
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.views.decorators.csrf import ensure_csrf_cookie, get_token


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(UserViewSet, self).get_permissions()



class DropletList(generics.ListCreateAPIView):
    """
    ViewSet that returns a form for registration
    """
    queryset = Droplet.objects.all()
    serializer_class = DropletSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    permission_classes = (permissions.AllowAny,)



class DropletDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    ViewSet that GET, PUT, DELETE droplet(s)
    For GET:
        - returns entire set of droplets
    For PUT:
        - Must have all required fields passed in as well, or it will not be saved
    """
    queryset = Droplet.objects.all()
    serializer_class = DropletSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserDetail(generics.RetrieveUpdateAPIView):
    """
    Returns a User's details and associated Droplets in JSON format
    User most be logged in before they can see this view.

    Accepts the following GET params: token
        - This should be passed in the form "Authorization": "token" "<token from login success here>"
            - Note: the whitespace between 'token' and the actual token matters!
    Accepts the following POST params:
        - Required: token (see above in GET)
        - Optional: email, username, other User fields
    Returns the updated User instance
    """
    authentication_classes = (TokenAuthentication, )
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        return self.request.user


class DropletQuery(generics.ListAPIView):
    """
    Viewset that filters based on given latitude and longitude proximity
    """

    serializer_class = DropletSerializer

    @staticmethod
    def to_float(n):
        try:
            print("type of n" + type(n))
            return float(n)
        except ValueError:
            return None

    def get_queryset(self):
        queryset = Droplet.objects.all()
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)
        latitude = self.to_float(latitude)
        longitude = self.to_float(longitude)

        lower_bound = 0.1
        upper_bound = 0.1

        if latitude is not None and longitude is not None:
            queryset = queryset.filter(latitude__range=(latitude-lower_bound, latitude+upper_bound),
                                       longitude__range=(longitude-lower_bound, longitude+upper_bound))

        return queryset

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(DropletQuery, self).dispatch(request, *args, **kwargs)
