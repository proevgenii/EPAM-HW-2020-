from hw3.task03.task03 import Filter


def test_class_Filter_on_existing_functions():
    positive_even = Filter(
        (lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int))
    )
    assert (positive_even.apply(range(10))) == [2, 4, 6, 8]
