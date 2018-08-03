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

Guess a number is a classic game which we can play by entering the number in the terminal. The game keeps on going
until you have guessed the correct number. Based on the input value you will get a prompt 'too low' or 'too high'
will you've guess the number correctly.

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

For every card game, the card deck should be well shuffled. The program above does that for us.
:code:`itertools.product()` returns a deck of cards as a list of tuples. Each tuple have suit and rank :code:`('♠', 'A')`.
:code:`random.shuffle()` shuffles the deck of cards and returns it.



Draw a single card
-----------------------------------

.. code-block:: python

    import random, itertools
    def draw_card()
        deck = list(
            itertools.product("♠♣♥♦♤♧♢♡", "AKQJ🔟98765432")
        )
        random.shuffle(deck)
        return random.choice(deck)
    print(draw_card())

As explained in the above example, a deck is created and shuffled randomly. :code:`random.choice()` selects a random
card out of the deck.


Roll a d20 dice
-------------------

.. code-block:: bash

    python -c "import random;print(random.choice(range(1,21)))"

D20 dice has 20 faces with numbers from 1 to 20. range(1,21) generates a list of number from 1 to 20.
:code:`random.choice` randomly get the value from the list.
