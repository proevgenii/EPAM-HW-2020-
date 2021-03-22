import pytest

from hw5.oop_1 import Homework, Student, Teacher


def test_normal_time_student_class(
    first_name="Ivan", last_name="Ivanov", task_text="Learn OOP", day_to_do=4
):
    student = Student(first_name, last_name)
    assert student.first_name == first_name
    assert student.last_name == last_name
    teacher = Teacher(first_name, last_name)
    homework = teacher.create_homework(task_text, day_to_do)
    assert (
        student.do_homework(homework) == homework
    )  # Метод принимает объект Homework и возвращает его же,
    # если задание уже просрочено, то печатет 'You are late' и возвращает None


def test_expired_time_student_class(
    first_name="Valerii", last_name="Petrov", task_text="Writing Tests", day_to_do=0
):
    student = Student(first_name, last_name)
    teacher = Teacher(first_name, last_name)
    homework = teacher.create_homework(task_text, day_to_do)
    assert (
        student.do_homework(homework) == None
    )  # Метод принимает объект Homework и возвращает его же,
    # если задание уже просрочено, то печатет 'You are late' и возвращает None
