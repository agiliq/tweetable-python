leet_dict = dict(zip("aeilot", "431|07"))

def leet(txt):
    return txt.lower().translate(str.maketrans(leet_dict))

def test_leet():
    resp = leet('hello this is leet')
    assert resp == 'h3||0 7h1s 1s |337'
