def add(a, b):
    return a + b


def sub(a, b):
    return a - b

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test_factorial():
    assert factorial(4) == 24
    assert fatorial(0) == 1
