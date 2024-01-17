from django.urls import path
from contents import views as content_views
from courses import views

urlpatterns = [
    path("courses/", views.CourseListCreate.as_view()),
    path("courses/<uuid:course_id>/", views.CourseRetrieveUpdateDestroy.as_view()),
    path("courses/<uuid:course_id>/contents/", content_views.ContentCreate.as_view()),
    path("courses/<uuid:course_id>/contents/<uuid:content_id>/", content_views.ContentRetrieveUpdateDestroy.as_view()),
    path("courses/<uuid:course_id>/students/", views.StudentUpdate.as_view()),
]