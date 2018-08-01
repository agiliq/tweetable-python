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

Draw a single card
-----------------------------------

Roll a d20 dice
-------------------
