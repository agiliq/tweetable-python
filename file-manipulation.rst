file manipulation
-----------------

oxford comma
============


count words in file
===================

.. code-block:: python

    len(open('data/test.txt', 'r').read().split())

Returns the number of words in a text file, test.txt


count lines in file
===================

.. code-block:: python

    len(open('data/test.txt', 'r').read().split('\n'))

Returns the number of lines in a text file, test.txt


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


first ten lines of file
=======================

.. code-block:: python

    open('data/100west.txt', 'r').read().split('\n')[:10]

Returns first 10 lines of a file.


last ten lines of file
======================

.. code-block:: python

    open('data/100west.txt', 'r').read().split('\n')[-10:]

Returns last 10 lines of a file
