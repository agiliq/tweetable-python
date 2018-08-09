import urllib3, json

resp = urllib3.PoolManager().request('GET', 'https://maps.googleapis.com/maps/api/geocode/json?address=' + 'madhapur,hyderabad')
json_resp = json.loads(resp.data)['results']
print(json_resp[0]['geometry']['location'] if json_resp['status'] == 'OK' else [])
