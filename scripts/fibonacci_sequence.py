def fibonacci_series(n):
    x=[0,1]
    [x.append(x[-2]+x[-1]) for _ in range(n-2)]
    return x

def test_fibonacci_series():
    assert fibonacci_series(7) == [0,1,1,2,3,5,8]
