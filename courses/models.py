import uuid
from django.db import models

from accounts.models import Account

class CourseStatus(models.TextChoices):
    NOTSTARTED = "not started"
    INPROGRESS = "in progress"
    FINISHED = "finished"

class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(choices=CourseStatus.choices, default=CourseStatus.NOTSTARTED, max_length=11)
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="courses",
        null=True
    )
    students = models.ManyToManyField("accounts.Account", through="students_courses.StudentCourse")