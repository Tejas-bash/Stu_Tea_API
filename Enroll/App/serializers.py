from rest_framework import serializers
from .models import teacher, student


class TeacherSerializer(serializers.ModelSerializer):
    teacher_img = serializers.ImageField(use_url=True)

    class Meta:
        model = teacher
        fields = ["id", "name", "age", "course", "teacher_img"]

    def create(self, validated_data):
        stu_data = teacher.objects.create(**validated_data)
        return stu_data


class StudentSerializer(serializers.ModelSerializer):
    student_img = serializers.ImageField(use_url=True)
    teacher_details = serializers.SerializerMethodField()

    class Meta:
        model = student
        fields = [
            "id",
            "name",
            "age",
            "enroll_course",
            "student_img",
            "teacher_fk",
            "teacher_details",  # Include teacher details here
        ]

    def get_teacher_details(self, obj):
        # Custom method to get serialized teacher details for a student
        teacher = obj.teacher_fk
        if teacher:
            serializer = TeacherSerializer(teacher)
            return serializer.data
        return None
