from rest_framework import serializers, status
from rest_framework.response import Response
from accounts.models import Account
from courses.models import Course
from courses.permissions import IsAdmin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from courses.serializers import CourseSerializer, StudentInCourseSerializer



class CourseListCreate(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return self.queryset.all()
        return self.queryset.filter(students=user)
    
class StudentUpdate(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]
    queryset = Course.objects.all()
    serializer_class = StudentInCourseSerializer
    lookup_url_kwarg = "course_id"


class CourseRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"