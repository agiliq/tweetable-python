Misc
=============

fizzbuzz
--------------


Upside down text
-------------------

.. code-block:: python

    def replacement(x): return dict(zip(string.ascii_letters+string.digits, 'ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz∀qƆpƎℲפHIſʞ˥WNOԀQɹS┴∩ΛMX⅄Z0ƖᄅƐㄣϛ9ㄥ86')).get(x, ' ')
    print("".join([replacement(ch) for ch in "Guido is a smart guy"]))

Prints the upside down version of the text.


Zalgo text
-------------------

.. code-block:: python

    import random as r
    u='̡̢̧̨̖̗̘̙̜̝̞̟̠̣̤̥̦̩̪̫̬̭̮̯̰̱̲̳̹̺̻̼͇͈͉͍͎͓͔͕͖͙͚͜͟͢ͅM̴̵̶̷̸'
    o = "'̛̀́̂̃̄̅̆̇̈̉̊̋̌̍̎̏̐̑̒̓̔̽̾̿̀́͂̓̈́͆͊͋͌͐͑͒͗͛̕̚͘͝͞͠͡'"
    def zalgo(txt):
            return "".join(["".join([el] + [r.choice(o+u) for _ in range(r.randint(0,6))])
            for el in txt])


.. code-block:: ipython

    In [5]: zalgo("He comes, he comes, the center cannot hold, it is too late")
    Out[5]: "H͌̈͋͡e͈͌̀͜͠ ̜͛c͇̱͑̆̎̕o͕̫̅me̲͊̀̓̓̅s͐,͖ ̟̓h̞̞e͔͛͂̋ ̘͙̻͆̇č̮͚͖̿o'm̀͢es̗̑̀,̂͜ t͕̻̾h͚̬̙̻e̡͕̰̼͂ ͔͛cḙ̠ņ̜͚̤̚ṭ̄e̖̩͠ŗ c'a̜͓̅̔n͇n̙̅̔̈́ǫ̠̦̣̏̇t͔͉͍́̈̐ '̺̂ͅhọ͕̹̿̏l̒d͙̹̗̄̈̕,̟ ̩̺͂̉̚͢i̤̲̪̤͗t͔̜ ̵̴͓̓̀ịs͚͍̤͙ ̛̟̗̫͒͋t͓̗͋̏̋̄oo̡͡ ̟́͂̂̕ĺ͇̳ate̝͕̥"


get time for functions to execute
----------------------------------

.. code-block:: python

    import timeit
    def test(x):
        return [each for each in range(x)]

    print(timeit.timeit('test(10000)', globals=globals(), number=10000))

:code:`timeit` module in python is used to calculating the time taken by a function complete its execution.
The value in :code:`number=` determines the number of time the specified method should execute.


Towers of Hanoi
--------------------

.. code-block:: python

    def move_tower(h,from_t,to_t,with_t):
        if h > 0:
            move_tower(h-1,from_t,with_t,to_t)
            move_disk(from_t,to_t)
            move_tower(h-1,with_t,to_t,from_t)

    def move_disk(f,t):
        print(f"move 💿  from {f} to {t}")


Round Robin Schedule generator
----------------------------------


Knockout Tournament Draw Generator
------------------------------------

Sorting without sort
------------------------

Insertion sort a list (without using :code:`sorted` or fammily)

.. code-block:: python

    def insertion_sort(data)
        for i,v in enumerate(data):
            while i>0:
                if data[i-1] > data[i]:
                    data[i-1],data[i] = data[i],data[i-1]
                else:
                    break
                i = i-1
        return data


Sorting without sort again
----------------------------

Quick sort a list (without using :code:`sorted` or fammily)

Build a simple todo manager using SQLIte
------------------------------------------
