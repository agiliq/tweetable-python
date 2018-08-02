String manipulation
++++++++++++++++++++++++

Invert letter case of string
===============================

Rot13 a String
====================

left pad
========

Speaking in ubbi dubbi
================================

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

.. code-block:: python

    import ipaddress
    ip_addr = input('Enter an IPv4 address: ')
    try:
        ipaddress.ip_address(ip_addr)
    except ValueError:
        print('Invalid IP v4 address')
    else:
        print('Valid IP v4 address')



Check if a string is a valid IP v6 address
========================================================================

.. code-block:: python

    import ipaddress
    ip_addr = input('Enter an IPv6 address: ')
    try:
        ipaddress.ip_address(ip_addr)
    except ValueError:
        print('Invalid IP v6 address')
    else:
        print('Valid IP v6 address')



Check if string is palindrome
==============================

.. code-block:: bash

    python -c "s=input('Enter a string: ');print('{} is {} a Palindrome'.format(s, '' if s==s[::-1] else 'not'))"


Find all valid anagrams of a word
=======================================


