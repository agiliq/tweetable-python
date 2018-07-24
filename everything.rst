everything
------------

module
===================

python -m http.server

python -m json.tools

python -m idlelib.idle

String manipulation
=====================

left pad
convert repeated spaces to one space


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

zip all .txt files in directory

batch rename files in directory

prettify json

file manipulation
===================

oxford comma

count words in file

count lines in file

add spaces after punctuation

add line numbers to text file
add line numbers to text file, don't number empty lines

delete trailing spacess

delete multiple newlines between paragraphs to keep only one line

first ten lines of file

last ten lines of file

games
=======

guess the number (binary search)

ascii art
================

asterisk triangle
banners (cowsay)

Mathematic
==============

pascal's triangle

unit convertor

ester eggs
============

import this

networking
==============

get local hostname

  os.uname().nodename
  
or 

  import socket; print(socket.gethostname())
  
  






