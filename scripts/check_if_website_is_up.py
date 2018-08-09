import urllib3

def check_website_is_up(address):
    try:
        resp = urllib3.PoolManager().request(address)
    except:
        print(False)
    else:
        print(resp.status == 200)
