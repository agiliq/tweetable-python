import math

def lcm(x,y):
    return (x*y)//math.gcd(x,y)


def test_lcm():
    assert lcm(5,7) == 35
