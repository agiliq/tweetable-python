def binary_to_decimal(binary):
    return int('0b'+binary, 2)


def test_binary_to_decimal():
    resp = binary_to_decimal('101')
    assert resp == 5
