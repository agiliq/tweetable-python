String manipulation
++++++++++++++++++++++++

Text manipulation and working with strings is one of the most common things in programming. Let us start with some simple things.

Invert letter case of string
===============================

Swap case of each character in a given text.

.. code-block:: python

    "THE quick brown fox, JUMPS ovEr the lazy dog".swapcase()

To use it on terminal.

.. code-block:: bash

    $ python -c "import sys; print(sys.argv[1].swapcase())" "THE quick brown fox, JUMPS ovEr the lazy dog"
    the QUICK BROWN FOX, jumps OVeR THE LAZY DOG

Rot-13 a String
====================

From wikipedia:

.. note: ROT13 ("rotate by 13 places", sometimes hyphenated ROT-13) is a simple letter substitution cipher that replaces a letter with the 13th letter after it, in the alphabet.

We will look at two ways of doing it.

.. code-block:: python

    from string import ascii_uppercase as upr, ascii_lowercase as lwr
    def rot13(txt):
        map = dict(list(zip(upr, upr[13:]+upr[:13]))+list((zip(lwr, lwr[13:]+lwr[:13]))))
        return "".join([map[el] for el in txt])

There is a lot going on here, so let's break it down.

.. code-block:: python

    from string import ascii_uppercase as upr, ascii_lowercase as lwr

Standard python imports, not much to see here.

.. code-block:: python

    list(zip(upr, upr[13:]+upr[:13]))

This gives a us a list of two-tuples   

.. code-block

[('A', 'N'),
 ('B', 'O'),
 ('C', 'P'),
 ...
]

We do the same thing for lower case letters. 

.. code-block:: python

    map = dict(list(zip(upr, upr[13:]+upr[:13]))+list((zip(lwr, lwr[13:]+lwr[:13]))))

Now we lookup the substitution letter from the map and switch join the together to get the Rot-13 word.    

.. code-block:: python

    return "".join([map[el] for el in txt])

Alternatively, we can go full "Betteries Included", and using the codecs module do :code:`codecs.encode(txt, 'rot_13')`

.. code-block:: python

    import codecs
    def rot13(txt):
        return codecs.encode(txt, 'rot_13')


left pad
========

Left pad allow you to specify minimum length to your string and a fill char to pad with to enforce that minimum limit.
This is easy to do using the `rjust` (right justify) methods on all strings.

.. code-block:: python

    def left_pad(txt, count, fill=' '):
        return txt.rjust(count, fill)

.. code-block:: bash

    $ python -c "import sys;print(sys.argv[1].rjust(int(sys.argv[2]), sys.argv[3]))" foobar 60 →
    →→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→foobar


Speaking in ubbi dubbi
================================

Ubbi dubbi is a language game spoken with the English language, Ubbi dubbi works by adding -ub- before each vowel sound in a syllable.

You can read about ubbi dubbi at: https://en.wikipedia.org/wiki/Ubbi_dubbi

This was recnetly popularised in "the Big bang Theory" https://www.youtube.com/watch?v=rfR03gibh6Ms. 
Let's look at how we would do it with Python.

.. code-block:: python

    vowels = "aeiou"
    vowels_dict = {i: f"ub{i}" for i in "aeiou"}
    def ubbi_dubbi(txt):
        return txt.lower().translate(str.maketrans(vowels_dict))

How are we doing it? We first generate a mapping of vowels to their ubbu-dubbi form.

.. code-block:: python

    vowels = "aeiou"
    vowels_dict = {i: f"ub{i}" for i in "aeiou"}


We then use :code:`str.maketrans(vowels_dict)` to generate the translation table, 
then use :code:`txt.lower().translate` to generate the ubbu-dubbi. Let's see the function in action.    

.. code-block:: bash

    In [4]: ubbi_dubbi("Subaru")
    Out[4]: 'subububarubu'

    In [5]: ubbi_dubbi("Speak")
    Out[5]: 'spubeubak'

    In [6]: ubbi_dubbi("Hubba Bubba bubblegum")
    Out[6]: 'hububbuba bububbuba bububblubegubum'



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
