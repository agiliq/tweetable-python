List, sets and other groups
=============================


Get unique elements from a list
---------------------------------

.. code-block:: bash

    python -c "print(set([1,1,4,5,6,2,2,4,3,5]))"

:code:`set()` denoted by :code:`{}` is a list of unique elements. When a list is converted into
a set all the repeated values are discarded.


Find most common elements in a list with their count
-------------------------------------------------------

.. code-block:: bash

    python -c "import collections;print(collections.Counter([1,2,2,3,3,4,4,4,4,4,6,6,6,6,6,6,6,6,6,7]))"

:code:`collections.Counter()` takes the list as input and creates a dictionary with list element as key
and number of occurrences of the element in list as the value.


Get only elements which are duplicated from a list
---------------------------------------------------

.. code-block:: bash

    python -c "import collections;x=dict(collections.Counter([1,2,3,4,5,5,6,6,6,7]));print([k for k,v in x.items() if v>1])"

Return only those items in the list that are repeated.


Reverse a list
-------------------

.. code-block:: bash

    python -c "x=[1,2,3,4,5,6,7,8,9];print(x[::-1])"

:code:`x[::-1]` is used to slicing a list. Negative value creates a copy of the list in reverse order.


Generate all permutations from a list
--------------------------------------

.. code-block:: bash

    python -c "import itertools;print(list(itertools.permutations(range(1,4))))"

:code:`itertools.permutations()` generates all the possible permutations of the given list.


Generate power set of a set
--------------------------------------

.. code-block:: bash

    python -c "import itertools;print([list(itertools.combinations([1,2,3], x)) for x in range(len([1,2,3])+1)])"

:code:`itertools.combinations()` generates all the possible combinations of a given list.
It take another optional argument, :code:`r` represents number of items per combination.


Sort a dictionary by keys
--------------------------------

.. code-block:: bash

    python -c "y={1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1};print(dict(sorted(y.items())))"

Sorts the dict by key.


Sort a dictionary by value
--------------------------------

.. code-block:: bash

    python -c "y={1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1};print(dict(sorted(y.items(), key=lambda kv: kv[1])))"

Sorts the dict by value. :code:`sorted()` takes an optional keyword argument :code:`key` which take a callable
to specify search key. In this case the search key is dict value instead of dict key.


Cartesian product of two lists
--------------------------------

.. code-block:: bash

    python -c "import itertools;print(list(itertools.product([['x','y','z'],[1,2,3]])))"

Generates cartesian product of two lists.
