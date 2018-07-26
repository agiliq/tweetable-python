mathematic
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


unit convertor
==============
