"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""

from collections import defaultdict
from datetime import datetime, timedelta


class DeadlineError(Exception):
    """
    :return DeadlineError if homework time expired
    """


class Homework:
    def __init__(self, task_text: str, day_to_do: int):
        self.text = task_text
        self.day_to_do = day_to_do
        self.deadline = timedelta(day_to_do)
        self.created = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

    def is_active(self):
        return bool(timedelta(days=self.day_to_do))


class HomeworkResult:
    def __init__(self, solution: str, author, homework):
        self.solution = solution
        self.author = author
        self.homework = homework
        self.created = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        if not isinstance(self.homework, Homework):
            raise AttributeError("You gave a not Homework object")


class Teacher:
    homework_done = defaultdict(set)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(task_text: str, day_to_do: int):
        return Homework(task_text, day_to_do)

    def check_homework(self, homeworkresult):
        if len(homeworkresult.solution) > 5:
            self.homework_done.append(homeworkresult.solution)
            return True
        else:
            return False

    def reset_results(self, hw):
        if isinstance(hw, Homework):
            self.homework_done.pop(hw.solution)
        elif hw is None:
            self.homework_done.clear()


class Student(Teacher):
    @classmethod
    def do_homework(cls, homework, result: str):
        HomeworkResult.author = cls
        if homework.is_active():
            return HomeworkResult(solution=result, author=cls, homework=homework)
        else:
            raise DeadlineError("You are late")


if __name__ == "__main__":
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")
    print(lazy_student.first_name, good_student.first_name)

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)
    print(oop_hw.text, docs_hw.text)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    print(result_1.solution)
    print(result_2.solution)
    print(result_3.solution)

    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print("There was an exception here")
    opp_teacher.check_homework(result_2)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results("sf")
