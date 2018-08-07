import math

def gdc(x,y):
    return math.gcd(x,y)

def test_gcd():
    assert gdc(12,8) == 4
