# Generated by Django 5.0.2 on 2024-02-14 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("course", models.CharField(max_length=100)),
                ("teacher_img", models.ImageField(upload_to="Teacher_image/")),
            ],
        ),
        migrations.CreateModel(
            name="student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("enroll_course", models.CharField(max_length=100)),
                ("student_img", models.ImageField(upload_to="student_image/")),
                (
                    "teacher_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="App.teacher"
                    ),
                ),
            ],
        ),
    ]
