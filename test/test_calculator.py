from calculator import add, sub, average
from calculator import add, sub, multiply
from calculator import add, sub, root

def test_add():
    assert add(2, 3) == 5
def test_sub():
    assert sub(10, 4) == 6

def test_average():
    assert average(0,10) == 5
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
def test_root():
    assert root(100, 2) == 10
    assert root(-5, 2) == "If a is negative b can't be even!"
def test_factorial():
    assert factorial(4) == 24
    assert fatorial(0) == 1
