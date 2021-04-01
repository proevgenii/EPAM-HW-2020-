from hw6.counter import instances_counter


@instances_counter
class A:
    pass


def test_for_counter():
    assert A.get_created_instances() == 0
    a = A()
    assert A.get_created_instances() == 1
    b = A()
    c = A()
    assert A.get_created_instances() == 3
    assert A.reset_instances_counter() == 3
    assert A.get_created_instances() == 0
