from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.views import APIView, csrf_exempt
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import DropletSerializer, UserSerializer
from .models import Droplet


class DropletList(generics.ListCreateAPIView):
    """
    ViewSet that returns all droplets on a GET, and allows POSTs for new droplets if a user is authenticated
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Droplet.objects.all()
    serializer_class = DropletSerializer

    def create(self, request, *args, **kwargs):
        """
        Grabs an authenticated User instance from request.user, and adds its id (primary key) to the request.data
        dictionary.
        """
        user = request.user
        request.data.update({'owner': user.id})
        return super(DropletList, self).create(request, *args, **kwargs)

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        """
        Overriden dispatch method with a csrf_exempt decorator
        """
        return super(DropletList, self).dispatch(request, *args, **kwargs)


class DropletQuery(generics.ListAPIView):
    """
    Viewset that filters based on given latitude and longitude proximity
    """

    serializer_class = DropletSerializer

    @staticmethod
    def to_float(n):
        """
        Simply convert a string to a float, while catching ValueError exceptions
        :param n: value to be converted
        :return: float, or NoneType if ValueError exception
        """
        try:
            return float(n)
        except ValueError:
            return None

    def get_queryset(self):
        """
        filter the queryset based on latitude and longitude proximity
        :return: droplets near location parameters
        """
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


class Profile(generics.ListAPIView):
    """
    View that returns all droplets belonging to the currently authenticated user
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = DropletSerializer

    def get_queryset(self):
        user = self.request.user
        return Droplet.objects.filter(owner=user.id)





