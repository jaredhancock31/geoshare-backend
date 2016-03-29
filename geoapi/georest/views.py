
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import generics
from django.http import Http404
from models import Droplet #, User
from serializers import AppUserSerializer, DropletSerializer
from permissions import IsOwnerOrReadOnly, IsStaffOrTargetUser
from django.contrib.auth.models import User
from rest_framework import viewsets


class DropletList(generics.ListCreateAPIView):
    queryset = Droplet.objects.all()
    serializer_class = DropletSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class DropletDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Droplet.objects.all()
    serializer_class = DropletSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class DropletMixin(object):
    queryset = Droplet.objects.all()
    serializer = DropletSerializer
    permission = (IsOwnerOrReadOnly, )

    def pre_save(self, obj):
        obj.owner = self.request.user


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = AppUserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AppUserSerializer

#
# class UserView(viewsets.ModelViewSet):
#     serializer_class = AppUserSerializer
#     model = User
#
#     def get_permissions(self):
#         # allow non-authenticated user to create via Post
#         return (permissions.AllowAny() if self.request.methd == 'POST'
#                 else IsStaffOrTargetUser())


@api_view(['GET'])
def droplet_query(request, lat, long):
    """
    get droplets within a certain range of lat and long params
    :param request: GET
    :param lat: latitude of current user
    :param long: longitude of current user
    :return: droplets (json) within range of lat and long
    """
    # TODO use filtering to retrieve the queryset according to the params
    pass


