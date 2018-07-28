Password generation and validation
-------------------------------------

Random Alpha-numeric passwords
==============================

.. code-block:: python

    import random, string; "".join([random.choice(string.ascii_letters + string.digits) for i in range(8)])

Creates a random alpha-numberic string of 8 characters that can be used as a password.


Pronounceable passwords
========================

.. code-block:: python

    import random;words=open('/usr/share/dict/words').read().split(); "-".join([random.choice(words) for _ in range(4)])


Creates a random '-' separated 4 word password from the given input text file to be used as a password


Passwords with alternate vowels
===============================

.. code-block:: python

    import random, string, itertools;
    "".join(itertools.chain(*zip([random.choice(string.ascii_lowercase) for _ in range(6)],  [random.choice('aeiou') for _ in range(6)])))

Caesar Cipher
===============================
