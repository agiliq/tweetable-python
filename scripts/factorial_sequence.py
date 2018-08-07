import math

def factorial(n):
    return math.factorial(int(n))

def test_factorial():
    assert factorial(7) == 5040
