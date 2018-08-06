String manipulation
++++++++++++++++++++++++

Invert letter case of string
===============================

.. code-block:: python

    "THE quick brown fox, JUMPS ovEr the lazy dog".swapcase()

Swaps case of each character in a given text.

To use it on terminal.

.. code-block:: bash

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

ROT13 is a simple letter substitution cipher that replaces a letter with the 13th letter after it, in the alphabet.
This program prints the Rot13 representation of the input text.

left pad
========

.. code-block:: python

    def left_pad(txt, count, fill=' '):
        return txt.rjust(count, fill)

.. code-block:: bash

    $ python -c "import sys;print(sys.argv[1].rjust(int(sys.argv[2]), sys.argv[3]))" foobar 60 →
    →→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→foobar


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

.. code-block:: python

    vwls=set('aeiou')
    def pig(wd):
      if len(wd)<2 or len(vwls&set(wd))==0:return f"{wd}way"
      elif wd[0] in vwls:return f"{wd}ay"
      else: x = min(wd.find(v) for v in vwls if v in wd);return f"{wd[x:]}{wd[:x]}way"
    def pig_ltn(txt): return " ".join(pig(e) for e in txt.lower().split())



Convert to leetspeak
========================

.. code-block:: python

    leet_dict = dict(zip("aeilot", "431|07"))
    def leet(txt):
        return txt.lower().translate(str.maketrans(leet_dict))


convert repeated spaces to one space
====================================

.. code-block:: python

    import re; re.sub(r"[ ]+", ' ', 'this    sentence          has              non-uniform      spaces')

The above snippet clears out the repeated spaces in a text and replaces it with single space.
re is a regular expression module to find more than one occurrences of space with '[ ]+'.


Check if a string is a valid IP v4 address
========================================================================

.. code-block:: python

    def ipv4_check(ip):
        try:
            ipaddress.IPv4Address(ip)
            return True
        except ipaddress.AddressValueError:
            return False

Or if you want only traditionally formatted ip addresses.

.. code-block:: python

    def ipv4_check(ip):
        try:
            chunks = str(ip).split(".")
            return all(int(chunk)<255 for chunk in chunks) and len(chunks) == 4
        except ValueError:
            return False


Check if a string is a valid IP v6 address
========================================================================

.. code-block:: python

    def ipv6_check(ip):
        try:
            ipaddress.IPv6Address(ip)
            return True
        except ipaddress.AddressValueError:
            return False

.. code-block:: bash

    In [32]: ipv6_check('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
    Out[32]: True

    In [33]: ipv6_check('2001:0db8:85a3:0000:0000:8a2e:0370:733455')
    Out[33]: False


Or if you want only traditionally formatted ip addresses.

.. code-block:: python

    def ipv6_check(ip):
        try:
            chunks = str(ip).split(":")
            return all(int(chunk, 16)<16**4 for chunk in chunks) and len(chunks) == 8
        except ValueError:
            return False


Check if string is palindrome
==============================

.. code-block:: python

    def is_palindrome(txt):
        return txt == txt[::-1]

A palindrome is a word, number, or other sequence of characters which reads the same backward as forward.
Python's extended slicing syntax :code:`[::-1]` returns the reverse of a given string or an iterable.


Find all valid anagrams of a word
=======================================

.. code-block:: python

    import itertools
    words=set(open('/usr/share/dict/words').read().split());
    def anagrams(txt):
        return set(["".join(perm) for perm in itertools.permutations(txt.lower())
            if "".join(perm) in words])
