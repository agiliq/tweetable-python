from string import ascii_uppercase as upr, ascii_lowercase as lwr

def rot13(txt):
    _map = dict(list(zip(upr, upr[13:] + upr[:13])) + list((zip(lwr, lwr[13:] + lwr[:13]))))
    return "".join([_map[el] if el in upr+lwr else el for el in txt])


def test_rot13():
    assert rot13('this text will transform') == 'guvf grkg jvyy genafsbez'
