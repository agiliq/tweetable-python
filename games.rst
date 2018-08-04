games
===========

guess the number
---------------------

.. code-block:: python

    import random
    def play():
      num, atmps = random.randint(1, 1000), 0
      while True:
        atmps += 1
        guess = int(input("Your guess "))
        if num == guess : print(f"you win. {atmps} attempts"); return
        x = "too high" if guess > num  else "too low"
        print(x)

.. code-block:: ipython

    In [22]: play()
    Your guess 500
    too low
    Your guess 750
    too high
    Your guess 625
    too low
    Your guess 700
    too high
    Your guess 650
    too high
    Your guess 635
    too high
    Your guess 630
    too high
    Your guess 627
    you win. 8 attempts


get a shuffled deck of cards
-----------------------------------

.. code-block:: python

    import random, itertools
    def shuffled_deck():
        deck = list(
            itertools.product("♠♣♥♦♤♧♢♡", "AKQJ🔟98765432")
        )
        random.shuffle(deck)
        return "\n".join([f"{n} of {suit}" for suit, n in deck])


Draw a single card
-----------------------------------

.. code-block:: python

    import random, itertools
    def shuffled_deck():
        deck = list(
            itertools.product("♠♣♥♦♤♧♢♡", "AKQJ🔟98765432")
        )
    return random.choice(deck)

.. code-block:: bash

    In [1]: import random, itertools
       ...: def draw_card():
       ...:     deck = list(
       ...:         itertools.product("♠♣♥♦♤♧♢♡", "AKQJ🔟98765432")
       ...:     )
       ...:     suit, n = random.choice(deck)
       ...:     return f"{n} of {suit}"
       ...:

    In [2]: draw_card()
    Out[2]: '5 of ♧'

    In [3]: draw_card()
    Out[3]: '🔟 of ♧'

    In [4]: draw_card()
    Out[4]: '5 of ♡'



Roll a d20 dice
-------------------
