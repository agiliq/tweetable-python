def is_palindrome(txt):
    return txt == txt[::-1]


def test_is_palindrome():
    resp = is_palindrome('racecar')
    assert resp
    resp = is_palindrome('halloween')
    assert not resp
