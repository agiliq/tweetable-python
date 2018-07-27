networking
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

code-block:: python

    import urllib.request, json
    json.loads(urllib.request.urlopen('http://jsonip.com').read())['ip']


Run it as

.. code-block:: bash

    $ python -c "import urllib.request, json; print(json.loads(urllib.request.urlopen('http://jsonip.com').read())['ip'])"
183.83.214.40
