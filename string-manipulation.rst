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

Pig Latin is a language game in which words in English are altered, usually by adding a fabricated suffix. The reference to Latin is a deliberate misnomer.

The rules are simple

- For words that begin with consonant sounds, all letters before the initial vowel are placed at the end of the word sequence. Then, "ay" is added,
- When words begin with consonant clusters (multiple consonants that form one sound), the whole sound is added to the end.Then, "ay" is added,
- For words that begin with vowel sounds, adds "way" to the end 

.. code-block:: python

    vwls=set('aeiou')
    def pig(wd):
      if len(wd)<2 or len(vwls&set(wd))==0:return f"{wd}way"
      elif wd[0] in vwls:return f"{wd}ay"
      else: x = min(wd.find(v) for v in vwls if v in wd);return f"{wd[x:]}{wd[:x]}way"
    def pig_ltn(txt): return " ".join(pig(e) for e in txt.lower().split())

There is a lot going on here, and to fit the code in 280 chars the variable names are very short. Lets break it down:

.. code-block:: python

    vwls=set('aeiou')

We are creatiing a set of vowels. Then we use it to apply the 3 rules described above.

.. code-block:: python

    def pig(wd):
      if len(wd)<2 or len(vwls&set(wd))==0:return f"{wd}way"
      elif wd[0] in vwls:return f"{wd}ay"
      else: x = min(wd.find(v) for v in vwls if v in wd);return f"{wd[x:]}{wd[:x]}way"

There are few interesting things we are doing. 

- :code:`len(vwls&set(wd))==0` This finds if there are no vowels in the word.
- :code:`len(vwls&set(wd))==0` This finds the first instance of a vowel, and :code:`f"{wd[x:]}{wd[:x]}way"` splices the consonants from the beginning to the end, then adds way.


Convert to leetspeak
========================

Leetspeak works by replacing certain letters. So we will use the same technique as rot13, and use :code:`.translate`

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

To find valid addresses, we can use :code:`ipaddress.IPv4Addres` which fails, if the strings can't be parsed ad an IP address.

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

In here, 
- we split the IP address on :code:`.`,
- then :code:`all(int(chunk)<255 for chunk in chunks) and len(chunks) == 4` checks if every chunk is an integer less than 255 and there are 4 chunks.

Check if a string is a valid IP v6 address
========================================================================

We use the same technique as above, but use :code:`ipaddress.IPv6Addres`

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

Again we use the same technique as IPv4, 
- splitting the address on :code:`:`
- Ensuring each chunk is parsable as a hexadecimal string, and less than :code:`16**4`.

Check if string is palindrome
==============================

A palindrome is a word, number, or other sequence of characters which reads the same backward as forward.

.. code-block:: python

    def is_palindrome(txt):
        return txt == txt[::-1]


Python's extended slicing syntax :code:`[::-1]` returns the reverse of a given string or an iterable. By comparing the two, we find out if a string is a palindrome.


Find all valid anagrams of a word
=======================================

To generate all valid anagrams,

- use :code:`itertools.permutations` to genrate the permutations
- Use :code:`words=set(open('/usr/share/dict/words').read().split())` to get a woldlist
- Check if the existing permutation exists and then we will return a set.

.. code-block:: python

    import itertools
    words=set(open('/usr/share/dict/words').read().split())
    def anagrams(txt):
        return set(["".join(perm) for perm in itertools.permutations(txt.lower())
            if "".join(perm) in words])


.. code-block:: ipython

    In [5]: anagrams('hello')
    Out[5]: {'hello'}

    In [6]: anagrams('rat')
    Out[6]: {'art', 'rat', 'tar'}

    In [7]: anagrams('post')
    Out[7]: {'opts', 'post', 'pots', 'spot', 'stop', 'tops'}
