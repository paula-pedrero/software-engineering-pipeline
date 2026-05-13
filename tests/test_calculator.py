from calculator import add, sub, modulo

def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(20, 7) == 6

def test_divide():
    assert div(10, 2) == 5
    assert div(9, 3) == 3
