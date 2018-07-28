String manipulation
++++++++++++++++++++++++

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


convert repeated spaces to one space
====================================

.. code-block:: python

    import re; re.sub(r"[ ]+", ' ', 'this    sentence          has              non-uniform      spaces')

The above snippet clears out the repeated spaces in a text and replaces it with single space.
re is a regular expression module to find more than one occurrences of space with '[ ]+'.


Find if a string is a valid IP v4 address
========================================================================

Find if a string is a valid IP v6 address
========================================================================

