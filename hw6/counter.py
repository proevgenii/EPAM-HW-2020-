"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""
import functools


def instances_counter(cls):
    cls.counter = 0

    def __new__(cls):
        new_cls = super(cls, cls).__new__(cls)
        cls.counter += 1
        return new_cls

    def get_created_instances():
        return cls.counter

    cls.get_created_instances = get_created_instances

    def reset_instances_counter():
        tmp_instances_counter = cls.counter
        cls.counter = 0
        return tmp_instances_counter

    cls.__new__ = __new__
    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class User:
    def __init__(self):
        self.params = 3


if __name__ == "__main__":
    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(User.get_created_instances())  # 3
    print(User.reset_instances_counter())  # 3
    print(user.__class__)
    print(user.params)
