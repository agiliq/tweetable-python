Mathematic
----------

Decimal to Binary
=======================

Binary to decimal
========================

Factorial sequence
=======================

Fibonacci Sequence
====================

GCD of two number
=====================

LCM of two numbers
=====================

Find the sum of all the multiples of 3 or 5 below 1000.
==========================================================

Distance between two points in three dimensional space
==========================================================

.. code-block:: python

    def distance(p1, p2) :
        (sum((wi - vi)**2 for  in zip(p1, p2)))**.5
    print distance((0,0,0), (5,4,3))


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


unit converter
==============


transpose a matrix
==================

Sieve of Eratosthenes
========================
