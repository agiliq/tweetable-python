File manipulation
-----------------

oxford comma
============


count words in file
===================

.. code-block:: python

    len(open('data/test.txt', 'r').read().split())

Returns the number of words in a text file, test.txt.
:code:`open('data/test.txt', 'r').read()` gets us the text of the file, we get the word using :code:`.split()`, and :code:`len` gives us the count of the words.

To run it for arbitrary files


.. code-block:: bash

    $ python -c "import sys; print(len(open(sys.argv[1], 'r').read().split()))" data/test.txt
    47


count lines in file
===================

.. code-block:: python

    len(open('data/test.txt', 'r').read().split('\n'))

Returns the number of lines in a text file, test.txt
:code:`open('data/test.txt', 'r').read()` gets us the text of the file, we get the word using :code:`.split('\n')`, and :code:`len` gives us the count of lines.

To run it for arbitrary files


.. code-block:: bash

    $ python -c "import sys;len(open(sys.argv[1], 'r').read().split('\n'))" data/test.txt
    54


add spaces after punctuation
============================

.. code-block:: python

    def repl(*args): obj=args[0]; return obj.string[obj.start()]+' '+obj.string[obj.start()+1]
    import re, string; re.sub('['+string.punctuation+'][a-zA-Z0-9]+', repl, "this'will;be.formatted,with! spaces")

Parse text and add a space after punctuations if its not present. If the space after the punctuation is present
it will remain intact.


add line numbers to text file
=============================

.. code-block:: python

    out=open('data/test-out.txt', 'w')
    for i, j in enumerate(open('data/test.txt', 'r')): out.write(str(i+1) + j)
    out.close()

Creates a new file with line number before each line.


add line numbers to text file, don't number empty lines
=======================================================

.. code-block:: python

    out=open('data/test-out.txt', 'w'); i=0
    for line in open('data/test.txt', 'r'):
        if line.strip(): out.write(str(i)+line);i+=1
        else: out.write(line)
    out.close()

Creates a new file with line number before each line. If the line is empty it will be skipped.


delete trailing spaces
======================


delete multiple newlines between paragraphs to keep only one line
=================================================================

.. code-block:: python

    out=open('data/out-single-line-gap.txt', 'w')
    out.write((re.sub('(\n\n)[\n]*', '\n\n', open('data/test.txt','r').read())))

Delete multiple new lines from a file between paragraphs and save it in a new file.

To run it for arbitrary files


.. code-block:: bash

    $ python -c "import sys;out=open('data/out-single-line-gap.txt', 'w');out.write((re.sub('(\n\n)[\n]*', '\n\n', open(sys.argv[1],'r').read())))" data/test.txt


first ten lines of file
=======================

.. code-block:: python

    open('data/100west.txt', 'r').read().split('\n')[:10]

Returns first 10 lines of a file.

To run it for arbitrary files


.. code-block:: bash

    $ python -c "import sys; open(sys.argv[1], 'r').read().split('\n')[:10]" data/test.txt


last ten lines of file
======================

.. code-block:: python

    open('data/100west.txt', 'r').read().split('\n')[-10:]

Returns last 10 lines of a file

To run it for arbitrary files


.. code-block:: bash

    $ python -c "import sys; open(sys.argv, 'r').read().split('\n')[-10:]" data/test.txt

Reverse a file line by line
===================================

.. code-block:: bash

    python -c "import sys;c=open('reverse.txt','w');c.write('\n'.join([x for x in open(sys.argv[1], 'r').read().split('\n')[::-1]]));c.close()" data/100west.txt

Creates a file with line in reverse order from that of the input file.


Get alternate lines from files starting from the top
======================================================

.. code-block:: bash

    python -c "import sys;c=open('alternate.txt','w');c.write('\n'.join([x for x in open(sys.argv[1], 'r').read().split('\n')[::2]]));c.close()" data/100west.txt

Creates a new file with alternate lines of the input file.


Find the most common words in a file
======================================

.. code-block:: bash

    python -c "import string,collections,sys,re;z=re.sub('[\n{}]'.format(string.punctuation), '',  open(sys.argv[1],'r').read().lower());x=collections.Counter(z.split(' '));del x[''];print(sorted(x.items(), key=lambda kv: kv[1], reverse=True)[:15])"

Returns the 15 most used words in a text file.


Find the lines which match a specified text
============================================================================

.. code-block:: bash

    python -c "import sys;search_text=input('Enter text to search:  ');print([x for x in open(sys.argv[1], 'r').read().split('\n') if search_text.lower() in x.lower()])" data/100west.txt

Returns all the lines containing an input text.


Convert file permissions to octal
===================================

rw-r--r-- = 644
rwxrwxrwx = 777

.. code-block:: bash

    python -c "_input=input('Enter file permissions: ');print(''.join([{'r--': '4', 'rw-': '6', 'r-x':'5', 'rwx':'7'}[x] for x in [_input[i:i+3] for i in range(0, len(_input), 3)]]))"

Program to convert unix file permissions :code:`rwxr--r--` to octal system. :code:`r`, :code:`w` and :code:`x` represents
read, write and execute permissions. The permissions are divided into 3 types, owner permission, group permission and
others permission. Example, if the file has these permissions, :code:`rw-r--r--`, the owner can read/write that file but
can not execute it. Member of a group to which that file belongs can only read the file. Similarly, others (who is neither
the owner nor a member of the group to which the file belongs) also can only read that particular file.


Convert octal file permissions to rwx format
=============================================

644 = rw-r--r--
777 = rwxrwxrwx

.. code-block:: bash

    python -c "_input=input('Enter file permissions: ');print(''.join([{'4':'r--', '6':'rw-','5':'r-x','7':'rwx'}[x] for x in str(_input)]))"

Program to convert octal file permissions :code:`644` to unix permissions. :code:`4`, :code:`5` and :code:`6` and :code:`7`
represents :code:`r--`, :code:`r-x`, :code:`rw-` and :code:`rwx` permissions respectively.
