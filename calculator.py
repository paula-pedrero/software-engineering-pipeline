def add(a, b):
    return a + b


def sub(a, b):
    return a - b

def root(a, b):
    if b % 2 == 0 and  a < 0:
        raise ValueError ("If a is negative b can't be pair!")
    return a**(1/b)