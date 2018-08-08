from string import ascii_uppercase as upr, ascii_lowercase as lwr

def caesar_cipher(txt, offset=1):
    _map = dict(list(zip(upr, upr[offset:] + upr[:offset])) + list((zip(lwr, lwr[offset:] + lwr[:offset]))))
    return "".join([_map[el] if el in upr+lwr else el for el in txt])

def test_caesar_cipher():
    assert caesar_cipher('attack at dawn') == 'buubdl bu ebxo'
    assert caesar_cipher('attack at dawn', offset=5) == 'fyyfhp fy ifbs'
