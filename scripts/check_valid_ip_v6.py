import ipaddress

def ipv6_check(ip):
    try:
        ipaddress.IPv6Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False


def test_ipv4_check():
    resp = ipv6_check('2607:f0d0:1002:51::4')
    assert resp
    resp = ipv6_check('2001:db8:a0b:12f0:0000:0001')
    assert not resp
