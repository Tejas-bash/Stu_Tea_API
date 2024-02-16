from django.db import models


class teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    teacher_img = models.ImageField(upload_to="Teacher_image/")

    def __str__(self) -> str:
        return f"{self.name}"


class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    enroll_course = models.CharField(max_length=100)
    student_img = models.ImageField(upload_to="student_image/")
    teacher_fk = models.ForeignKey(teacher, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"
