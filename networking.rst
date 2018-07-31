Networking
+++++++++++


get local hostname
-----------------------

.. code-block:: python

    import os; os.uname().nodename

    # or

    import socket; print(socket.gethostname())


Run this as

.. code-block:: bash

    $ python -c "import os; print(os.uname().nodename)"
    shabdas-MacBook-Pro.local


Get IP Address
-----------------------

.. code-block:: python

  import socket; s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);s.connect(("8.8.8.8", 80));print(s.getsockname()[0])

Run it as

.. code-block:: bash

    $ python -c "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);s.connect(('8.8.8.8', 80));print(s.getsockname()[0])"
    192.168.31.253


Get IP Address using a remote service
--------------------------------------

.. code-block:: python

    import urllib.request, json
    json.loads(urllib.request.urlopen('http://jsonip.com').read())['ip']


Run it as

.. code-block:: bash

    $ python -c "import urllib.request, json; print(json.loads(urllib.request.urlopen('http://jsonip.com').read())['ip'])"
    183.83.214.40

Find number of addresses in a subnet
-------------------------------------

List all addresses in a subnet
-------------------------------------

Generate a Random IPv6 Address
-------------------------------

Generate a mac Address
-----------------------------

.getnode() can fake the MAC addr by returning a random 48-bit number, calling it twice ensure we are not hitting the random path

.. code-block:: python

    from uuid import getnode

    def get_mac():
        return hex(getnode()) if getnode() == getnode() else None

Generate a gravatar url from email
-----------------------------------


Get IP address for a hostname
-----------------------------------

    import socket
    socket.gethostbyname('agiliq.com')


Check if website is up
----------------------------
