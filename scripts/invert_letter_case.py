def invert_letter_case(n):
    return n.swapcase()

def test_invert_letter_case():
    assert invert_letter_case('AloHA') == 'aLOha'
