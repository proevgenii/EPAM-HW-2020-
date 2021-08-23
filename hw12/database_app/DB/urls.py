from django.contrib import admin
from django.urls import include, path

from DB.views import (
    CreateHomeworkView, CreateStudentView, CreateTeacherView, DoHomeworkView)

urlpatterns = [
    path("create_teacher/", CreateTeacherView.as_view()),
    path("create_student/", CreateStudentView.as_view()),
    path("create_homework/", CreateHomeworkView.as_view()),
    path("do_homework/", DoHomeworkView.as_view()),
]
