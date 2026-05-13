from calculator import add, sub, average

def test_add():
    assert add(2, 3) == 5
def test_sub():
    assert sub(10, 4) == 6

def test_average():
    assert average(0,10) == 5