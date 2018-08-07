import itertools


def cartesian_product(_list):
    return list(itertools.product(*_list))


def test_cartesian_product():
    resp = cartesian_product([['x','y','z'],[1,2,3]])
    assert resp == [('x',1),('x',2),('x',3),
                    ('y',1),('y',2),('y',3),
                    ('z',1),('z',2),('z',3)]
