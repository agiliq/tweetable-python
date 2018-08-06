import random

def play():
    num, atmps = random.randint(1, 1000), 0
    while True:
        atmps += 1
        guess = int(input("Your guess "))
        if num == guess: print(f"you win. {atmps} attempts"); return
        x = "too high" if guess > num else "too low"
        print(x)
play()