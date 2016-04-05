from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import DropletSerializer
from .models import Droplet


class DropletList(generics.ListCreateAPIView):
    """
    ViewSet that returns all droplets
    """
    queryset = Droplet.objects.all()
    serializer_class = DropletSerializer


class DropletQuery(generics.ListAPIView):
    """
    Viewset that filters based on given latitude and longitude proximity
    """

    serializer_class = DropletSerializer

    @staticmethod
    def to_float(n):
        try:
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


@api_view(['GET'])
def droplet_query(request, latitude, longitude):
    pass
