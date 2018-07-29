Misc
=============

fizzbuzz
--------------


Upside down text
-------------------

.. code-block:: python

    def replacement(x): return dict(zip(string.ascii_letters+string.digits, 'ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz∀qƆpƎℲפHIſʞ˥WNOԀQɹS┴∩ΛMX⅄Z0ƖᄅƐㄣϛ9ㄥ86')).get(x, ' ')
    print("".join([replacement(ch) for ch in "Guido is a smart guy"]))

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


