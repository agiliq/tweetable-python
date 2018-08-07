def distance(p1, p2):
    return (sum((wi - vi) ** 2 for wi, vi in zip(p1, p2))) ** .5

print(distance((0, 0, 0), (5, 4, 3)))

def test_distance():
    assert distance((1,3,5), (7,1,4)) == 6.4031242374328485
