from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow
    the creator of an event to perform any action.
    Other users can neither
    read nor perform CRUD operations.
    """

    def has_object_permission(self, request, view, obj):
        # Allow access only if the user is the creator of the event
        return obj.creator == request.user

    def has_permission(self, request, view):
        # Allow access only if the user is authenticated
        return request.user and request.user.is_authenticated
