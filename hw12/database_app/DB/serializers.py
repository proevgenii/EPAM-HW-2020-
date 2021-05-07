from rest_framework import serializers

from DB.models import Homework, HomeworkResult, Student, Teachers


class TeacherDetailSerializer(serializers.ModelSerializer):
    homework_done = serializers.HiddenField(default=False)

    class Meta:
        model = Teachers
        fields = "__all__"


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class HomeworkDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = "__all__"


class DoHomeworkDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkResult
        fields = "__all__"
