Mathematic
----------

Decimal to Binary
=======================

.. code-block:: bash

    python -c "_in=int(input('Enter Decimal value: '));print(bin(_in))"

Decimal number system has number from 0 to 9 while binary number system has only two numbers 0 and 1.
The code above will convert a given decimal value into a binary value.


Binary to decimal
========================

.. code-block:: bash

    python -c "_in=input('Enter Binary value: ');print(int('0b'+_in, 2))"

Decimal number system has number from 0 to 9 while binary number system has only two numbers 0 and 1.
For a given binary input it will return the corresponding decimal value.
:code:`0b` is before the binary number as python3 representation of binary is prefixed with :code:`0b`.
So, :code:`100` in binary is represented as :code:`0b100`


Factorial sequence
=======================

.. code-block:: bash

    python -c "import math;_in=input('Enter value: ');print(math.factorial(int(_in)))"

The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n.
The program above will return factorial of the input integer.


Fibonacci Sequence
====================

.. code-block:: bash

    python -c "n=int(input('Enter number of terms: '));x=[0,1];[x.append(x[-2]+x[-1]) for _ in range(n-2)];print(x)"

Fibonacci Series is a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
The simplest is the series 0, 1, 1, 2, 3, 5, 8, etc.


GCD of two number
=====================

.. code-block:: bash

    python -c "import math;x=int(input('Enter First No. '));y=int(input('Enter Second No. '));print(math.gcd(x,y))"

The greatest common divisor (GCD) of two or more integers, which are not all zero, is the largest positive integer
that divides each of the integers. Above program will print the GCD of two given numbers.


LCM of two numbers
=====================

 .. code-block:: bash

    python -c "import math;x=int(input('Enter First No. '));y=int(input('Enter Second No. '));print((x*y)//math.gcd(x,y))"

The Least Common Multiple (LCM) of a group of numbers is the smallest number that is a multiple of all the numbers.


Find the sum of all the multiples of 3 or 5 below 1000.
==========================================================

.. code-block:: bash

    python -c "import math;print(sum(set([x*3 for x in range(math.ceil(1000/3)) if x<1000]+[x*5 for x in range(math.ceil(1000/5)) if x*5<1000]+[x*15 for x in range(math.ceil(1000/15)) if x*15<1000])))"

Returns every number that is a multiple of 3 or 5. As the LCM of 3 and 5 is 15, all the multiples of 15 are also included
in the results.


Distance between two points in three dimensional space
==========================================================

.. code-block:: python

    def distance(p1, p2) :
        return (sum((wi - vi)**2 for wi,vi in zip(p1, p2)))**.5
    print(distance((0,0,0), (5,4,3)))


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

.. code-block:: python

    flag = 1
    n = int(input('Enter the number: '))
    for i in range(2,n):
        if(n%i == 0):
            print('%d is not a prime number' %n)
            flag = 0
            break
    if(flag == 1):
        print('%d is a prime number' %n)

A prime number is a whole number greater than 1 whose only factors are 1 and itself.


Find largest number among numbers passed on command line
===========================================================

.. code-block:: bash

    python -c "x=[int(each) for each in input('Enter comma separated list of numbers: ').strip().split(',') if each];print(max(x))"


unit converter
==============


transpose a matrix
==================

.. code-block:: bash

    python -c "x=[[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]];print([each for each in zip(*x)])"

Transpose of a Matrix. A matrix which is formed by turning all the rows of a given matrix into columns and vice-versa.
:code:`zip` returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
Returned value of zip would look like :code:`[[1,6,11], [2,7,12], ... ]`


Sieve of Eratosthenes
========================

.. code-block:: python

    n=int(input('Enter a number: '))
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    print([p for p in range(2, n) if prime[p]])

The sieve of Eratosthenes is a simple, ancient algorithm for finding all prime numbers up to any given limit.
