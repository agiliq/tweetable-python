def decimal_to_binary(n):
    return bin(n)

def test_decimal_to_binary():
    assert decimal_to_binary(15) == '0b1111'
