import uuid
from django.db import models
from accounts.models import Account
from courses.models import Course


class StudentCourseStatus(models.TextChoices):
    PENDING = "pending"
    ACCEPTED = "accepted"

class StudentCourse(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(choices=StudentCourseStatus.choices, default=StudentCourseStatus.PENDING)
    student = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="students_courses")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students_courses")