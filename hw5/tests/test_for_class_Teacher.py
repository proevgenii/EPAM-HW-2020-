import pytest

from hw5.oop_1 import Homework, Teacher


@pytest.mark.parametrize(
    ["first_name", "last_name", "task_text", "day_to_do"],
    [("Ivan", "Ivanov", "Learn OOP", 4), ("Petr", "Petrov", "Writing tests", 0)],
)
def test_teacher_class(first_name, last_name, task_text, day_to_do):
    teacher = Teacher(first_name, last_name)
    assert teacher.first_name == first_name
    assert teacher.last_name == last_name
    homework = teacher.create_homework(
        task_text, day_to_do
    )  # Метод принимает задание и количество дней на выполнение
    assert isinstance(homework, Homework)  # Метод возвращает экземпляр Homework
