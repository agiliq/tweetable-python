# Generates a random 8 digit password
import random, string

"".join([random.choice(string.ascii_letters + string.digits) for i in range(8)])
