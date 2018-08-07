def unique_elements_in_list(lst):
    return list(set(lst))

def test_unique_elements_in_list():
    assert unique_elements_in_list([1,2,3,3,3,4,4,4,2,6,7]) == [1,2,3,4,6,7]
