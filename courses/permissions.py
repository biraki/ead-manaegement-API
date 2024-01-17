from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
        def has_permission(self, request, view):
            return bool(
                request.method in permissions.SAFE_METHODS or
                request.user.is_authenticated and
                request.user.is_superuser
        )
class IsAdminOrInCourse(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return request.user in obj.course.students.all()
