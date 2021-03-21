from hw3.task02.task02 import function_for_parallelize_calculating_sum


def test_time_for_calculating_sum():
    assert function_for_parallelize_calculating_sum() <= 60.0  # checking time for calculating
