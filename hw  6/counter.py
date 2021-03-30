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
    counter = 0

    @functools.wraps(cls)
    def cls(*args, **kwargs):
        nonlocal counter
        counter += 1

    def get_created_instances():
        return counter

    cls.get_created_instances = get_created_instances

    def reset_instances_counter():
        nonlocal counter
        counter_to_return = counter
        counter = 0
        return counter_to_return

    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class User:
    pass


if __name__ == "__main__":
    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(User.get_created_instances())  # 3
    print(User.reset_instances_counter())  # 3
