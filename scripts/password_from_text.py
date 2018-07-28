# Generate Pronounceable passwords from a text file
import random
words=open('/usr/share/dict/words').read().split(); "-".join([random.choice(words) for _ in range(4)])
