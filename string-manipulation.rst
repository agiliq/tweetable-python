String manipulation
++++++++++++++++++++++++

Invert letter case of string
===============================

.. code-block:: python

    "THE quick brown fox, JUMPS ovEr the lazy dog".swapcase()

To use it on terminal.

    python -c "import sys; print(sys.argv[1].swapcase())" "THE quick brown fox, JUMPS ovEr the lazy dog"


Rot13 a String
====================

.. code-block:: python

    from string import ascii_uppercase as upr, ascii_lowercase as lwr
    def rot13(txt):
        map = dict(list(zip(upr, upr[13:]+upr[:13]))+list((zip(lwr, lwr[13:]+lwr[:13]))))
        return "".join([map[el] for el in txt])

Alternatively

.. code-block:: python

    import codecs
    def rot13(txt):
        return codecs.encode('foobar', 'rot_13')

left pad
========

Speaking in ubbi dubbi
================================

.. code-block:: python

    vowels = "aeiou"
    vowels_dict = {i: f"ub{i}" for i in "aeiou"}
    def ubbi_dubbi(txt):
        return txt.lower().translate(str.maketrans(vowels_dict))

.. code-block:: bash

    In [4]: ubbi_dubbi("Subaru")
    Out[4]: 'subububarubu'

    In [5]: ubbi_dubbi("Speak")
    Out[5]: 'spubeubak'

    In [6]: ubbi_dubbi("Hubba Bubba bubblegum")
    Out[6]: 'hububbuba bububbuba bububblubegubum'


https://www.youtube.com/watch?v=rfR03gibh6M
https://en.wikipedia.org/wiki/Ubbi_dubbi

Pig latin
================

https://en.wikipedia.org/wiki/Pig_Latin

Convert to leetspeak
========================


convert repeated spaces to one space
====================================

.. code-block:: python

    import re; re.sub(r"[ ]+", ' ', 'this    sentence          has              non-uniform      spaces')

The above snippet clears out the repeated spaces in a text and replaces it with single space.
re is a regular expression module to find more than one occurrences of space with '[ ]+'.


Check if a string is a valid IP v4 address
========================================================================

Check if a string is a valid IP v6 address
========================================================================

Check if string is palindrome
==============================

Find all valid anagrams of a word
=======================================


