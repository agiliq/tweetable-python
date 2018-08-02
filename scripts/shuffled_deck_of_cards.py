import random, itertools

def shuffled_deck():
    deck = list(
        itertools.product("♠♣♥♦♤♧♢♡", "AKQJ🔟98765432")
    )
    random.shuffle(deck)
    return "\n".join([f"{n} of {suit}" for suit, n in deck])

print(shuffled_deck())
