Ascii and unicode art
--------------------------

asterisk triangle
=================

.. code-block:: python

    print('\n'.join([''.join(['*' for _ in range(x+1)]) for x in range(5)]))

Generates an incremental triangle of asterisk '*'. Example:

.. code-block:: python

    *
    **
    ***
    ****
    *****

.. code-block:: python

    print('\n'.join([''.join(['*' for _ in range(5-x)]) for x in range(5)]))


Prints out asterisk triangle in decremental order. Example:

.. code-block:: python

    *****
    ****
    ***
    **
    *


.. code-block:: python

    print('\n'.join([ (11-x)*' '+ ''.join(['* ' for _ in range(x)]) for x in range(1,11, 2)]))

Prints out a asterisk triangle as below:

.. code-block:: python

      |            *
      |          * * *
      |        * * * * *
      |      * * * * * * *
      |    * * * * * * * * *


Alternating Pattern
===================

.. code-block:: python

    print('\n'.join([(x+1)*'#'+(7-x)*'*' for x in range(7)]))

Prints alternating patterns in # and * based on a given integer n. n=7 here.

.. code-block:: python

    #*******
    ##******
    ###*****
    ####****
    #####***
    ######**
    #######*

Display current directory as a tree
=======================================

.. code-block:: python
    import os

    def list_files(startpath):
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))

Similar to running tree


banners (cowsay)
================

Display list of tuples as tables on terminal
================================================

.. code-block:: python

    def list_as_table(data):
        for ele1,ele2,ele3 in data:
            print("{:<14}{:<14}{}".format(ele1,ele2,ele3))

Usage

.. code-block:: bash

    In [1]: data=[('one', 'two', 'three'),('four', 'five', 'six'),('seven','eight','nine')]

    In [2]: def list_as_table(data):
        ...:     for ele1,ele2,ele3 in data:
        ...:         print("{:<14}{:<14}{}".format(ele1,ele2,ele3))
        ...:

    In [3]: list_as_table(l)
    one           two           three
    four          five          six
    seven         eight         nine

Here formatting a strig uses `Format Specification Mini-Language <https://docs.python.org/3.6/library/string.html#format-specification-mini-language>`. :code:`:<14` here first two columns will take 14 spaces
and the text will be left-aligned.


Generate sparklines
=====================


Series of integers to sparklines visible on command line

.. code-block:: python

    spark_chars = "▁▂▃▄▅▆▇██"
    def sparkline(series):
        mn, mx = min(series), max(series)
        interval = (mx-mn)//8
        bucketed = [(el-mn)//interval for el in series]
        spark_dict = dict(zip(range(9), spark_chars))
        return "".join([spark_dict[el] for el in bucketed])


horizontal bar graphs
======================

.. code-block:: bash


    81 ██████
    92 ████████
    99 █████████
    64 ███
    59 ██
    88 ███████
    91 ███████
    67 ███

.. code-block:: python

    ch = "█"
    def bar(series):
        mn, mx = min(series), max(series)
        interval = (mx-mn)//8
        bucketed = [(el-mn)//interval for el in series]
        return "\n".join(
            [f"{n} {b}" for n, b in zip(series, [ch*(el+1) for el in bucketed])]
        )

Column Graphs
===============

.. code-block:: python

    ch= "█"
    def col(sz):
        mn,mx=min(sz),max(sz)
        df = (mx-mn)//8
        bkt = [(el-mn)//df for el in sz]
        hrz = [f"{b}{c}" for b,c in
                [(ch*(el+1)," "*(8-el))  for el in bkt]
            ]
        return "\n".join([" ".join(el) for el in list(map(list, zip(*hrz)))[::-1]])


.. code-block:: bash


    In [2]: import random

    In [3]: series = [random.randint(10, 99) for _ in range(25)]

    In [4]: print(col(series))

    █                         █   █
    █           █       █     █   █                 █
    █           █ █     █     █   █   █     █ █     █
    █       █   █ █     █     █   █   █     █ █     █
    █       █   █ █     █     █   █ █ █     █ █     █
    █       █   █ █     █     █   █ █ █     █ █     █
    █       █ █ █ █ █   █     █   █ █ █     █ █ █   █
    █       █ █ █ █ █   █ █   █ █ █ █ █ █   █ █ █ █ █
    █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █
