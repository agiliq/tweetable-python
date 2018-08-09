# Remove multiple spaces from text
import re

def remove_multiple_spaces(txt):
    return re.sub(r"[ ]+", ' ', txt)

def test_remove_multiple_spaces():
    formatted_txt = remove_multiple_spaces('this    sentence          has              non-uniform      spaces')
    assert formatted_txt == 'this sentence has non-uniform spaces'
