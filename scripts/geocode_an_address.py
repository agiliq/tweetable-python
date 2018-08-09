import urllib3, json

def geocode_from_address(address):
    resp = urllib3.PoolManager().request('GET', 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address)
    try:
        json_resp = json.loads(resp.data)['results']
    except:
        return []
    return json_resp[0]['geometry']['location'] if json_resp['status'] == 'OK' else []
