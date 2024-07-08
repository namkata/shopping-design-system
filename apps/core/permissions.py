from rest_framework.permissions import IsAuthenticated


class IsAdminUser(IsAuthenticated):
    def has_permission(self, request, view):
        # First, check if the user is authenticated
        is_authenticated = super().has_permission(request, view)
        # Then, check if the user is either staff or superuser
        return is_authenticated and (
            request.user.is_staff or request.user.is_superuser
        )
