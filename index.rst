Tweetable Python
==================

A book of 128 short (280 chars or less) python commands which get the job done.

Inspired by Peteris Krumins' Perl One Liners.

The book is a collection of 128 small python programs. Each of these programs does something useful and/or fun.

Take this example 

.. code-block:: python

    import random, string
    "".join([random.choice(string.ascii_letters + string.digits) for i in range(8)])

In less than a 100 chars, you can generate truly random passwords.

We will look at things like file manipulation, file conversion, password generation and even a game.

Lets get started.



.. toctree::
   :maxdepth: 2
   :caption: Table of Contents:

   everything
   file-manipulation
   file-conversion
   password
   ascii-art
   mathematics
   string-manipulation



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
