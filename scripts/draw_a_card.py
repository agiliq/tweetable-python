import random, itertools

def draw_card():
    deck = list(
        itertools.product("♠♣♥♦♤♧♢♡", "AKQJ🔟98765432")
    )
    return random.choice(deck)

print(draw_card())


def test_draw_card():
    assert draw_card() != draw_card()
