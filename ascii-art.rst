ascii art
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


banners (cowsay)
================
