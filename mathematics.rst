Mathematic
----------

pascal's triangle
=================

.. code-block:: python

    print('\n'.join([ (6-x)*' '+ ''.join(['{} '.format(p) for p in str(11**x)]) for x in range(6) if x!=1]))

Prints out Pascal's triangle as below

.. code-block:: python

    |              1
    |            1 2 1
    |           1 3 3 1
    |          1 4 6 4 1
    |         1 6 1 0 5 1


OEIS sequence A127421
=====================

.. code-block:: python

    [(x-1)*(10**len(str(x))) + x for x in range(1,19)]

Prints out an OEIS sequence A127421, numbers whose decimal expansion is a concatenation of 2 consecutive increasing non-negative numbers.
1, 12, 23, 34, 45, 56, 67, 78, 89, 910, 1011, 1112, ....

Check if a number is a prime
===================================

Find largest number among numbers passed on command line
===========================================================

Find largest number among numbers passed on command line
===========================================================


unit convertor
==============


transpose a matrix
==================

Sieve of Eratosthenes
========================
