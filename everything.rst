everything
------------

module
===================

python -m http.server

python -m json.tool

password
===================

import random, string; "".join([random.choice(string.ascii_letters + string.digits) for i in range(8)])

xkcd password


import random;words=open('/usr/share/dict/words').read().split(); "-".join([random.choice(words) for _ in range(4)])


pronouncable passwords

import random, string, itertools; 
"".join(itertools.chain(*zip([random.choice(string.ascii_lowercase) for _ in range(6)],  [random.choice('aeiou') for _ in range(6)])))

file conversions
===================

csv to json

json to csv

csv to sqlite

base64 encoding

base64 decoding

file manipulation
===================

oxford comma

count words in file

count lines in file

add spaces after punctuation.




