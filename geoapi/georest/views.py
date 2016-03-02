from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import User, Droplet
from serializers import UserSerializer, DropletSerializer


@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all users, or create a new one
    :param request:
    :return:
    """

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    get, update, or delete a specific user
    :param request: get,put,delete
    :param pk: user_id (primary key)
    :return: response
    """

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def droplet_list(request):
    """
    List all droplets, or create a new one
    :param request:
    :return:
    """

    if request.method == 'GET':
        droplets = Droplet.objects.all()
        serializer = DropletSerializer(droplets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DropletSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def droplet_detail(request, pk):
    """
    get, update, or delete a specific user
    :param request: get,put,delete
    :param pk: drop_id (primary key)
    :return: response
    """

    try:
        droplet = Droplet.objects.get(pk=pk)
    except Droplet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DropletSerializer(droplet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DropletSerializer(droplet, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        droplet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
