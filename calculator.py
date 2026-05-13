def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def power(a,b):
    return a ** b


def modulo(a, b):
    return a % b


def div(a, b):
    return a / b


def average(a, b):
    return (a+b)/2


def multiply(a, b):
    return a * b


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def root(a, b):
    if b % 2 == 0 and  a < 0:
        return "If a is negative b can't be even!"
    return a**(1/b)