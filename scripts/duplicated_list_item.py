import collections

def duplicated_items_in_list(l):
    x=dict(collections.Counter(l))
    return [k for k,v in x.items() if v>1]


def test_duplicated_items_in_list():
    assert duplicated_items_in_list([1,2,3,4,5,5,6,6,6,7]) == [5,6]
