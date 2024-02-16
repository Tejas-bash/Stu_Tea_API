from django.contrib import admin
from .models import *


@admin.register(teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "course", "teacher_img"]


@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "enroll_course", "student_img", "teacher_fk"]
