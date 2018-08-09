import urllib3

def check_website_is_up(address):
    try:
        resp = urllib3.PoolManager().request('get', address)
    except:
        return False
    else:
        return resp.status == 200


def test_check_website_is_up():
    assert check_website_is_up('www.google.com')
