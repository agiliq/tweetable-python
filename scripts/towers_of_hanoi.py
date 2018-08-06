def move_tower(h, from_t, to_t, with_t):
    if h > 0:
        move_tower(h - 1, from_t, with_t, to_t)
        move_disk(from_t, to_t)
        move_tower(h - 1, with_t, to_t, from_t)


def move_disk(f, t):
    print(f"move 💿  from {f} to {t}")

move_tower(8,5,4,3)
