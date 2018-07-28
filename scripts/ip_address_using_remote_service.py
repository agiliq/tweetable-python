# Get an IP address using remote service
import urllib.request, json

print(json.loads(urllib.request.urlopen('http://jsonip.com').read())['ip'])
