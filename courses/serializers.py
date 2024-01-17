from rest_framework import serializers
from accounts.models import Account
from courses.models import Course
from students_courses.serializers import StudentCourseSerializer



class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["id", "name", "status", "contents" , "start_date", "end_date", "instructor", "students_courses"]
        extra_kwargs = {"students_courses": {"read_only": True, "source": "students"}, "status": {"read_only": True}, "contents": {"read_only": True}}
    

class StudentInCourseSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
        extra_kwargs = {"name": {"read_only": True}}

    def update(self, instance, validated_data):
        students = []
        not_found_students = []
        for student_course in validated_data["students_courses"]:
            student = student_course["student"]
            found_student = Account.objects.filter(email=student["email"]).first()
            if not found_student:
                not_found_students.append(student["email"])
            else:
                students.append(found_student)
        if not_found_students:
            raise serializers.ValidationError(
                {
                    "detail": f"No active accounts was found: {', '.join(not_found_students)}."
                }
            )
        if not self.partial:
            instance.students.add(*students)
            return instance
        return self.update(instance, validated_data)
