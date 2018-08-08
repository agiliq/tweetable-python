Using remote services
=========================

Get details of a book by its ISBN number
-------------------------------------------


Get truly random numbers
-----------------------------


Verify if password is insecure using HIBP
--------------------------------------------

.. code-block:: python

    import urllib3
    email='tweetable@python.com'
    resp=urllib3.PoolManager().urlopen('GET', 'https://haveibeenpwned.com/api/v2/breachedaccount/{}'.format(email),
        headers={'user-agent': 'Pwnage-Checker-For-Django'})
    print('Breached' if resp.data else 'Secure')


Get a user's latest tweet
------------------------------


Currency conversion
----------------------

Get top 10 urls for a search
-------------------------------------

Geocode an address
---------------------

.. code-block:: python

    import urllib3,json
    resp=urllib3.PoolManager().request('GET', 'https://maps.googleapis.com/maps/api/geocode/json?address='+'madhapur,hyderabad')
    json_resp=json.loads(resp.data)['results']
    print(json_resp[0]['geometry']['location'] if json_resp['status'] == 'OK' else [])

https://maps.googleapis.com/maps/api/geocode/json?address=madhapur,hyderabad


Quote of the day
---------------------

.. code-block:: python

    import requests as r

    def get_quote():
        resp=r.get('https://quotes.rest/qod')
        data = resp.json()
        print(data['contents']['quotes'][0]['quote'])

Fetch quote of the day from the rest API provided by theysaidso.com.


Copy a file to FTP with a datestamped name
---------------------------------------------------------------



Get the time using a NTP server
--------------------------------

http://code.activestate.com/recipes/117211-simple-very-sntp-client/

s.AF_INET is 2
s.SOCK_DGRAM is 2

.. code-block:: python

    import socket as s,struct,time

    def ntp(url):
        c=s.socket(2,2)
        d=b'\x1b'+47*b'\0'
        c.sendto(d,(url,123))
        d,address=c.recvfrom(1024)
        if d:
            t=struct.unpack('!12I',d)[10]
            t -= 2208988800
            return time.ctime(t),t
