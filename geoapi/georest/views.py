
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from models import User, Droplet
from serializers import UserSerializer, DropletSerializer


class UserList(APIView):
    """
    List all users, or create new user
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update, or delete a User instance
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DropletList(APIView):
    """
    List all users, or create new user
    """
    def get(self, request, format=None):
        droplets = Droplet.objects.all()
        serializer = DropletSerializer(droplets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DropletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DropletDetail(APIView):
    """
    Retrieve, update, or delete a Droplet instance
    """
    def get_object(self, pk):
        try:
            return Droplet.objects.get(pk=pk)
        except Droplet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        droplet = self.get_object(pk)
        serializer = DropletSerializer(droplet)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        droplet = self.get_object(pk)
        droplet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#
# @api_view(['GET', 'POST'])
# def user_list(request):
#     """
#     List all users, or create a new one
#     :param request:
#     :return:
#     """
#
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail(request, pk):
#     """
#     get, update, or delete a specific user
#     :param request: get,put,delete
#     :param pk: user_id (primary key)
#     :return: response
#     """
#
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def droplet_list(request):
#     """
#     List all droplets, or create a new one
#     :param request:
#     :return:
#     """
#
#     if request.method == 'GET':
#         droplets = Droplet.objects.all()
#         serializer = DropletSerializer(droplets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = DropletSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def droplet_detail(request, pk):
#     """
#     get, update, or delete a specific user
#     :param request: get,put,delete
#     :param pk: drop_id (primary key)
#     :return: response
#     """
#
#     try:
#         droplet = Droplet.objects.get(pk=pk)
#     except Droplet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = DropletSerializer(droplet)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = DropletSerializer(droplet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         droplet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET'])
# def droplet_query(request, lat, long):
#     """
#     get droplets within a certain range of lat and long params
#     :param request: GET
#     :param lat: latitude
#     :param long: longitude
#     :return: droplets (json) within range of lat and long
#     """
#     # TODO use filtering to retrieve the queryset according to the params
#     pass

