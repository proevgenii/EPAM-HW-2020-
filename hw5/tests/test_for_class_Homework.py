from datetime import datetime, timedelta

import pytest

from hw5.oop_1 import Homework, Student, Teacher


@pytest.mark.parametrize(
    ["task_text", "day_to_do", "is_active"],
    [("Learn OOP", 4, True), ("Write tests", 0, False)],
)
def test_homework_class(task_text, day_to_do, is_active):
    """Homework принимает на вход 2 атрибута: текст задания и количество дней
    на это задание"""
    hw = Homework(task_text, day_to_do)
    assert hw.text == task_text  # Атрибут с текстом задания
    assert hw.deadline == timedelta(
        days=day_to_do
    )  # Атибрут который хранит объект datetime.timedelta с количеством дней на выполнение
    assert hw.created == datetime.now().strftime(
        "%Y-%m-%d-%H:%M:%S"
    )  # Атрибут c точной датой и временем создания
    assert (
        hw.is_active() == is_active
    )  # Метод который проверяет не истело ли время на выполнение задания
