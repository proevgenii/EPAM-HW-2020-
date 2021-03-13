from hw3.task04.task04 import is_armstrong


def test_for_func_is_armstrong():
    assert is_armstrong(153) is True, "Is Armstrong number"
    assert is_armstrong(10) is False, "Is not Armstrong number"
    assert is_armstrong(0) is True, "Is Armstrong number"
    assert is_armstrong(1) is True, "Is Armstrong number"
