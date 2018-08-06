Tweetable Python
==================

128 puny python programs which pack a punch.
----------------------------------------------

Each programs in this books fits in a single tweet (280 chars or less) and does something useful, powerful or fun.

These programs will serve a reference, inspire and delight.
In most cases, but not always, the code is :code:`Pythonic`, without any obfuscation or code golfing.

These programs serve as a testament to Python's power, conciseness *and* clarity

Take this example

.. code-block:: python

    import random, string
    "".join(
      [random.choice(string.ascii_letters + string.digits)
      for i in range(8)]
    )

In less than a 100 chars, you can generate truly random passwords.

Now look at this function which fits a tweet.

.. code-block:: python

    ch= "█"
    def col(sz):
        mn,mx=min(sz),max(sz)
        df = (mx-mn)//8
        bkt = [(el-mn)//df for el in sz]
        hrz = [f"{b}{c}" for b,c in
                [(ch*(el+1)," "*(8-el))  for el in bkt]
            ]
        return "\n".join([" ".join(el) for el in list(map(list, zip(*hrz)))[::-1]])

You can now generate a columns chart for any integer series, visible on terminals.

.. code-block:: bash


    In [2]: import random

    In [3]: series = [random.randint(10, 99) for _ in range(25)]

    In [4]: print(col(series))

    █                         █   █
    █           █       █     █   █                 █
    █           █ █     █     █   █   █     █ █     █
    █       █   █ █     █     █   █   █     █ █     █
    █       █   █ █     █     █   █ █ █     █ █     █
    █       █   █ █     █     █   █ █ █     █ █     █
    █       █ █ █ █ █   █     █   █ █ █     █ █ █   █
    █       █ █ █ █ █   █ █   █ █ █ █ █ █   █ █ █ █ █
    █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █


We will look at things like file manipulation, file conversion, password generation, ascii art and even some games. This book is inspired by Peteris Krumins' Perl One Liners.

.. note:: Judge me by my size, do you? Hmm, hmm. - Yoda.

Lets get started.



.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Table of Contents:

   string-manipulation
   file-manipulation
   file-conversion
   password
   ascii-art
   mathematics
   networking
   date-and-calendar
   modules
   lists-set
   games
   remote
   misc
   ester-eggs


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
