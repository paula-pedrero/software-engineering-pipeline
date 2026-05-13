from calculator import add, sub, modulo, multiply, average, root, power, factorial, div


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(20, 7) == 6


def test_divide():
    assert div(10, 2) == 5
    assert div(9, 3) == 3


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6


def test_average():
    assert average(0, 10) == 5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0


def test_power():
    assert power(2, 2) == 4
    assert power(2, 4) == 16


def test_root():
    assert root(100, 2) == 10
    assert root(-5, 2) == "If a is negative b can't be even!"


def test_factorial():
    assert factorial(4) == 24
    assert factorial(0) == 1
