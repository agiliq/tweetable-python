python -m
=================


pretty print a json
---------------------------

:code:`python -m json.tool` will format a string

.. code-block:: bash


    $ cat data/example.json
    [{"fieldname0": "User", "fieldname1": "Country", "fieldname2": "Age"}, {"fieldname0": "Alex", "fieldname1": "US", "fieldname2": "25"}, {"fieldname0": "Ben", "fieldname1": "US", "fieldname2": "24"}, {"fieldname0": "Dennis", "fieldname1": "UK", "fieldname2": "25"}, {"fieldname0": "Yuvi", "fieldname1": "IN", "fieldname2": "24"}](django-admin-cookbook)

    $ cat data/example.json | python -m json.tool
    [
        {
            "fieldname0": "User",
            "fieldname1": "Country",
            "fieldname2": "Age"
        },
        {
            "fieldname0": "Alex",
            "fieldname1": "US",
            "fieldname2": "25"
        },
        {
            "fieldname0": "Ben",
            "fieldname1": "US",
            "fieldname2": "24"
        },
        {
            "fieldname0": "Dennis",
            "fieldname1": "UK",
            "fieldname2": "25"
        },
        {
            "fieldname0": "Yuvi",
            "fieldname1": "IN",
            "fieldname2": "24"
        }
    ]


Expose a folder to a static file server
-------------------------------------------

:code:`python -m http.server` will start a server on port 8000 which will server the files from current dir.

.. code-block:: bash

    $ python -m http.server 8844
    Serving HTTP on 0.0.0.0 port 8844 (http://0.0.0.0:8844/) ...


A simple editor for Python
-------------------------------------------

Every python install comes with the idle editor, you can start it like this :code:`python -m idlelib.idle`


Debugging emails
-------------------
.. code-block:: bash

    $ python -m smtpd -n -c DebuggingServer localhost:1025


Profiling scripts
----------------------

.. code-block:: bash

    $ python -m cProfile scriptname.py


Creating virtual environments
------------------------------
.. code-block:: bash

    $ python -m venv venv_name


Running doctests
------------------------------
Assuming you have my_functions.py with next content:

.. code-block:: python

    def is_palindrome(text):
        """
        Check if input text is palindrome

        >>> is_palindrome('eye')
        True

        >>> is_palindrome('tree')
        False
        """
        return text == text[::-1]

To run doctests:

.. code-block:: bash

    $ python -m doctest my_functions.py
    
    
Getting info on your python environment
--------------------------------------------

.. code-block:: bash

    python -m site
    
This prints
    
.. code-block:: bash

    sys.path = [
        '/Users/shabda/repos/cats/data',
        '/Users/shabda/.virtualenvs/cats-may/lib/python36.zip',
        '/Users/shabda/.virtualenvs/cats-may/lib/python3.6',
        '/Users/shabda/.virtualenvs/cats-may/lib/python3.6/lib-dynload',
        '/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6/lib/python3.6',
        '/Users/shabda/.virtualenvs/cats-may/lib/python3.6/site-packages',
    ]
    USER_BASE: '/Users/shabda/.local' (exists)
    USER_SITE: '/Users/shabda/.local/lib/python3.6/site-packages' (exists)
    ENABLE_USER_SITE: False
    
