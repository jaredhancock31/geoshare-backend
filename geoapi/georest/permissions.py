#!/usr/bin/env python
from rest_framework.permissions import AllowAny,BasePermission, SAFE_METHODS, IsAuthenticated

__author__ = 'jared hancock'


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsStaffOrTargetUser(BasePermission):
    # allow user to list all users if logged in user is Staff
    def has_permission(self, request, view):
        return view.action == 'retrieve' or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # allow logged in user to view own details, allows staff to view all records
        return request.user.is_staff or obj == request.user
