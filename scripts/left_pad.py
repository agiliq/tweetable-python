def left_pad(txt, count, fill=' '):
    return txt.rjust(count, fill)

def test_left_pad():
    assert left_pad('padding', 10, '^') == '^^^padding'
