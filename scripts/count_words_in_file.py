# Counts the number of words in a file
def count_words_in_file(_file):
    return len(open(_file, 'r').read().split())

def test_count_words_in_file():
    resp = count_words_in_file('data/100west.txt')
    assert resp == 3046
