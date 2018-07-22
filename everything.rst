everything
------------

module
++++++++++

python -m http.server

python -m json.tool

password
++++++++++

import random, string; "".join([random.choice(string.ascii_letters + string.digits) for i in range(8)])

xkcd password

import random;words=open('/usr/share/dict/words').read().split(); "-".join([random.choice(words) for _ in range(4)])