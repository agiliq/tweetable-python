Password generation, validation and more random things
---------------------------------------------------------

Random Alpha-numeric passwords
==============================

.. code-block:: python

    import random, string; "".join([random.choice(string.ascii_letters + string.digits) for i in range(8)])

:code:`random.choice(string.ascii_letters + string.digits)` picks a character from :code:`string.ascii_letter`
and :code:`string.digits`. Iterating over it will return 8 random alpha-numeric characters which can be used as a password.


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

Get a password where every alternate character is a vowel.


Validate password complexity
==============================

Validate that a password is least 8 chars, and contains at least 3 of lowercase, uppercase, numbers and symbols.



Caesar Cipher
===============================

.. code-block:: python

    from string import ascii_uppercase as upr, ascii_lowercase as lwr

    def caesar_cipher(txt, offset=1):
        _map = dict(list(zip(upr, upr[offset:] + upr[:offset])) + list((zip(lwr, lwr[offset:] + lwr[:offset]))))
        return "".join([_map[el] if el in upr+lwr else el for el in txt])


Caesar cipher is one of the earliest known and simplest ciphers. It is a substitution cipher with a given offset.
Each letter is shifted by the offset, default value is 1.

.. code-block:: python

    from string import ascii_uppercase as upr, ascii_lowercase as lwr

Standard python imports, not much to see here.

.. code-block:: python

    list(zip(upr, upr[offset:] + upr[:offset]))

This gives a us a list of two-tuples similar to the one shown below based on the value of :code:`offset`

.. code-block

    [('A', 'N'),
    ('B', 'O'),
    ('C', 'P'),
    ...
    ]

We do the same thing for lower case letters.

.. code-block:: python

        _map = dict(list(zip(upr, upr[offset:] + upr[:offset])) + list((zip(lwr, lwr[offset:] + lwr[:offset]))))

Now we lookup the substitution letter from the map and switch join the together to get the Rot-13 word.

.. code-block:: python

        return "".join([_map[el] if el in upr+lwr else el for el in txt])


Generate a UUID
========================

.. code-block:: python

    import uuid
    print(uuid.uuid4())

Generates a random uuid with 36 characters.


Generate a url safe UUID
=========================

(For example for use as a slug)

.. code-block:: python

    import uuid, base64
    base64.urlsafe_b64encode(uuid.uuid4().bytes)

This will give a 24 character UUID. If you need a shorter one, you can take a slice
The code below gives you an unique 16 character UUID

.. code-block:: python

    import uuid, base64
    base64.urlsafe_b64encode(uuid.uuid4().bytes)[:16]
