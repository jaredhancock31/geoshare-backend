#!/usr/bin/env python

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework import permissions
from rest_framework import generics
from rest_framework import exceptions
from django.http import Http404
from models import Droplet #, User
from serializers import AppUserSerializer, DropletSerializer
from permissions import IsOwnerOrReadOnly, IsStaffOrTargetUser
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.views.decorators.csrf import ensure_csrf_cookie, get_token

__author__ = 'jared hancock'


class DropletList(generics.ListCreateAPIView):
    """
    ViewSet that returns all droplets
    """
    queryset = Droplet.objects.all()
    serializer_class = DropletSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class DropletDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    ViewSet that GET, POST, PUT, DELETE droplet(s)
    For GET:
        - returns entire set of droplets
    For PUT:
        - Must have all required fields passed in as well, or it will not be saved
    """
    queryset = Droplet.objects.all()
    serializer_class = DropletSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


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
    serializer_class = AppUserSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        return self.request.user


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


@api_view(['GET'])
@ensure_csrf_cookie
def dummy(request):
    return Response("large butts")


# @api_view(['GET', 'POST'])
# def my_login(request):
#     auth = (BasicAuthentication,)
#     if request.method == 'POST':
#         username = request.POST['username']
#         if not username:
#             return None
#
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             raise exceptions.AuthenticationFailed('No such user')
#
#         return user, None


# class DropletMixin(object):
#     """
#     Don't worry about what this does right now, we aren't using it.
#     """
#     queryset = Droplet.objects.all()
#     serializer = DropletSerializer
#     permission = (IsOwnerOrReadOnly, )
#
#     def pre_save(self, obj):
#         obj.owner = self.request.user
