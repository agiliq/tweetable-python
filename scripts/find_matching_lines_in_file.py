def find_matching_lines(search_text, _file):
    return [x for x in open(_file, 'r').read().split('\n') if search_text.lower() in x.lower()]

def test_find_matching_lines():
    assert len(find_matching_lines('the', 'data/100west.txt')) == 228
