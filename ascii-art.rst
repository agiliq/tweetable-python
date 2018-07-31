Ascii art
---------------

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

Similar to running tree


banners (cowsay)
================

Display list of tuples as tables on terminal
================================================

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
