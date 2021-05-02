import sys
from datetime import datetime, timedelta

from django.db import models

# Create your models here.


class Teachers(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    homework_done = models.CharField(verbose_name="Решение ДЗ", max_length=100)

    def create_homework(task_text: str, day_to_do: int):
        return Homework(task_text=task_text, day_to_do=day_to_do)

    def check_homework(self, homeworkresult):
        if len(homeworkresult.solution) > 5:
            self.homework_done = homeworkresult.solution
            return True
        else:
            return False


class Student(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)


class Homework(models.Model):
    text = models.CharField(verbose_name="Текст задания", max_length=100)
    day_to_do = models.DurationField(
        verbose_name="Количество времени на выполнение задания"
    )
    created = models.DateTimeField(auto_now_add=True)
    teacher_the_creater = models.ForeignKey(
        Teachers, on_delete=models.CASCADE, default=1
    )

    def is_active(self):
        return bool(days=self.day_to_do)


class HomeworkResult(models.Model):
    solution = models.CharField(verbose_name="Решение задания", max_length=100)
    author = models.ForeignKey(
        Student, verbose_name="Автор задания", max_length=100, on_delete=models.CASCADE
    )
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
