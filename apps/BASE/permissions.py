from rest_framework import permissions


class NonAuthenticatedAPIMixin:
    """
    A mixin that allows unrestricted access to an API endpoint
    by setting the permission classes to AllowAny.
    """
    permission_classes = [permissions.AllowAny]

class AuthenticatedAPIMixin:
    """
    A mixin that allows restricted access to an API endpoint
    by setting the permission classes to IsAuthenticated.
    """
    permission_classes = [permissions.IsAuthenticated]
