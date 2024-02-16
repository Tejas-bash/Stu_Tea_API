from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import student, teacher
from .serializers import TeacherSerializer, StudentSerializer
from rest_framework.decorators import api_view


@api_view(["GET"])
def view_data(request):
    if request.method == "GET":
        stu_data = student.objects.all()
        if stu_data.exists():
            serializer = StudentSerializer(stu_data, many=True)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"No_Data": "Data isn't available"})


@api_view(["POST"])
def create_teacher_data(request):
    if request.method == "POST":
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
