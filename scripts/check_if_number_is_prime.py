
def check_for_prime_number(n):
    flag = 1
    for i in range(2,n):
        if n%i == 0:
            return False
            flag = 0
            break
    if flag == 1:
        return True


def test_check_for_prime_number():
    resp = check_for_prime_number(15)
    assert not resp
    resp = check_for_prime_number(31)
    assert resp
