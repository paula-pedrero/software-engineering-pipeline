def add(a, b):
    return a + b


def sub(a, b):
    return a - b

def root(a, b):
    if b % 2 == 0 and  a < 0:
        return "If a is negative b can't be even!"
    return a**(1/b)