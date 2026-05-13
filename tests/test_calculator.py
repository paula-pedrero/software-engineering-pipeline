from calculator import add, sub, modulo

def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(20, 7) == 6