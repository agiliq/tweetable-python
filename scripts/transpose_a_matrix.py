x=[[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]
def tranpose_a_matrix(matrix):
    return [each for each in zip(*matrix)]

def test_transpose_a_matrix():
    assert tranpose_a_matrix([[1,2], [6,7], [11,12]]) == [(1,6,11), (2,7,12)]
