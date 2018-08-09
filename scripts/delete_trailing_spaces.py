def remove_trailing_spaces(txt):
    return txt.rstrip()

def test_remove_trailing_spaces():
    formatted_txt = remove_trailing_spaces(' trailing spaces will be removed.                        ')
    assert formatted_txt == ' trailing spaces will be removed.'
