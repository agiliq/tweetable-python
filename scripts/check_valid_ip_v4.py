import ipaddress

def ipv4_check(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False


def test_ipv4_check():
    resp = ipv4_check('192.168.56.255')
    assert resp
    resp = ipv4_check('192.256.56.255')
    assert not resp
