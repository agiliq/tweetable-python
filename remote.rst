Using remote services
=========================

Get details of a book by its ISBN number
-------------------------------------------


Get truly random numbers
-----------------------------


Verify if password is insecure using HIBP
--------------------------------------------

Get a user's latest tweet
------------------------------


Currency conversion
----------------------

Get top 10 urls for a search
-------------------------------------

Geocode an address
---------------------

https://maps.googleapis.com/maps/api/geocode/json?address=madhapur,hyderabad


Quote of the day
---------------------

https://quotes.rest/qod



Get the time using a NTP server
--------------------------------

http://code.activestate.com/recipes/117211-simple-very-sntp-client/

.. code-block:: python

    import socket as s,struct,time

    def ntp():
        c=s.socket(s.AF_INET,s.SOCK_DGRAM)
        d=b'\x1b'+47*b'\0'
        c.sendto(d,('time.nist.gov',123))
        d,address=c.recvfrom(1024)
        if d:
            t=struct.unpack('!12I',d)[10]
            t -= 2208988800
            return time.ctime(t),t
