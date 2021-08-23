from django.shortcuts import render
from rest_framework import generics

from DB.serializers import (DoHomeworkDetailSerializer,
                            HomeworkDetailSerializer, StudentDetailSerializer,
                            TeacherDetailSerializer)


# Creation Teacher.
class CreateTeacherView(generics.CreateAPIView):
    serializer_class = TeacherDetailSerializer


# Creation Student.
class CreateStudentView(generics.CreateAPIView):
    serializer_class = StudentDetailSerializer


# Creation HomeWork.
class CreateHomeworkView(generics.CreateAPIView):
    serializer_class = HomeworkDetailSerializer


# Do homework.
class DoHomeworkView(generics.CreateAPIView):
    serializer_class = DoHomeworkDetailSerializer


# View all tables.
# class TablesListView(generics.ListAPIView):
#     serializer_class = ...
#     queryset =
