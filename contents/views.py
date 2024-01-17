from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from contents.models import Content
from contents.serializers import ContentSerializer
from courses.models import Course
from courses.permissions import IsAdmin, IsAdminOrInCourse
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class ContentCreate(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
     
    def perform_create(self, serializer):
        found_course = get_object_or_404(Course, pk=self.kwargs.get("course_id"))
        return serializer.save(course=found_course)


class ContentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrInCourse]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"

    def get_object(self):
        course = Course.objects.filter(pk=self.kwargs["course_id"]).first()
        content = Content.objects.filter(pk=self.kwargs["content_id"]).first()

        if not course:
            raise NotFound({"detail": "course not found."})
        if not content:
            raise NotFound({"detail": "content not found."})
        self.check_object_permissions(self.request, content)
        return content
    