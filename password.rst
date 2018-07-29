Password generation, validation and more random things
---------------------------------------------------------

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


Validate password complexity
==============================

Validate that a password is least 8 chars, and contains at least 3 of lowercase, uppercase, numbers and symbols.



Caesar Cipher
===============================

Generate a UUID
========================


Generate a url safe UUID
=========================

(For example for use as a slug)

.. code-block:: python

    import uuid, base64
    base64.urlsafe_b64encode(uuid.uuid4().bytes)

This will give a 24 char UUID. If you need a shorter one, you can take a slice

.. code-block:: python

    import uuid, base64
    base64.urlsafe_b64encode(uuid.uuid4().bytes)[:16]
