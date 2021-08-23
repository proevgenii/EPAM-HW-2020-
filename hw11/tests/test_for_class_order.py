from hw11.hw2 import Order


def morning_discount(order):
    return order.price - order.price * 0.5


def elder_discount(order):
    return order.price - order.price * 0.9


def test_for_class_order_with_dicount():
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50

    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10


def test_for_class_order_no_discount():
    order3 = Order(100)
    assert order3.final_price() == 100
