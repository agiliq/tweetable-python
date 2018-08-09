def insertion_sort(data):
    for i,v in enumerate(data):
        while i>0:
            if data[i-1] > data[i]:
                data[i-1],data[i] = data[i],data[i-1]
            else:
                break
            i = i-1
    return data

def test_insertion_sort():
    assert insertion_sort([5,1,3,9,4]) == [1,3,4,5,9]
