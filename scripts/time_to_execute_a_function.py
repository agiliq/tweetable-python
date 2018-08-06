import timeit
def test(x):
    return [each for each in range(x)]

print(timeit.timeit('test(10000)', globals=globals(), number=1), 'seconds')
