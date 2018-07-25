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
.. code-block:: python

    import re; re.sub(r"[ ]+", ' ', 'this    sentence          has              non-uniform      spaces')

The above snippet clears out the repeated spaces in a text and replaces it with single space.
re is a regular expression module to find more than one occurrences of space with '[ ]+'.


password
===================
.. code-block:: python

    import random, string; "".join([random.choice(string.ascii_letters + string.digits) for i in range(8)])

xkcd password

.. code-block:: python

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
.. code-block:: python

    import zipfile, os; myzip = zipfile.ZipFile('test.zip', 'w'); [myzip.write(each) for each in os.listdir() if each.endswith('.txt')]

Creates a zip file called test.zip of all the .txt files present in your current directory.
zipfile.ZipFile creates a new zip file. os.listdir() lists all the files in the current directory.


batch rename files in directory

prettify json
.. code-block:: python

    import json; json.dumps([{"one":123,"two":455,"three":789}], indent=4)

Returns a prettified json string for the given json object. The above json object will be converted into
[
    {
        "one": 123,
        "two": 455,
        "three": 789
    }
]



file manipulation
===================

oxford comma

count words in file
.. code-block:: python

    len(open('data/test.txt', 'r').read().split())

Returns the number of words in a text file, test.txt


count lines in file
.. code-block:: python

    len(open('data/test.txt', 'r').read().split('\n'))

Returns the number of lines in a text file, test.txt


add spaces after punctuation
.. code-block:: python

    def repl(*args): return args[0].group() + ' '
    import re, string; re.sub('['+string.punctuation+']+', repl, "this'will;be.formatted,with!spaces")


add line numbers to text file
.. code-block:: python

    out=open('data/test-out.txt', 'w')
    for i, j in enumerate(open('data/test.txt', 'r')): out.write(str(i+1) + j)
    out.close()

add line numbers to text file, don't number empty lines
.. code-block:: python

    out=open('data/test-out.txt', 'w')
    for i, j in enumerate(open('data/test.txt', 'r')): c.write(str(i+1) + j) if j.strip() else c.write(j)
    out.close()

delete trailing spaces

delete multiple newlines between paragraphs to keep only one line
.. code-block:: python

    out=open('data/out-single-line-gap.txt', 'w')
    out.write((re.sub('[\n]+', '\n', open('data/test.txt','r').read())))

first ten lines of file
.. code-block:: python

    open('data/100west.txt', 'r').read().split('\n')[:10]


last ten lines of file
.. code-block:: python

    open('data/100west.txt', 'r').read().split('\n')[-10:]


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
  
  
Get IP Address

  import socket; s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);s.connect(("8.8.8.8", 80));print(s.getsockname()[0])
  
(Or use urllib with json, read remote API.)  





