from calculator import add, sub, root

def test_add():
    assert add(2, 3) == 5
def test_sub():
    assert sub(10, 4) == 6
def test_root():
    assert root(100, 2) == 10
    assert root(-5, 2) == "If a is negative b can't be even!"