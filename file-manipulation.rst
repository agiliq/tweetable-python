File manipulation
-----------------

oxford comma
============


count words in file
===================

.. code-block:: python

    len(open('data/test.txt', 'r').read().split())

Returns the number of words in a text file, test.txt.
:code:`open('data/test.txt', 'r').read()` gets us the text of the file. We get the word using :code:`.split()`,
splits the text by any whitespace and returns a list of words. Empty strings are removed from the results.
Then, :code:`len` gives us the count of the words.

To run it for arbitrary files


.. code-block:: bash

    $ python -c "import sys; print(len(open(sys.argv[1], 'r').read().split()))" data/test.txt
    47


count lines in file
===================

.. code-block:: python

    len(open('data/test.txt', 'r').read().split('\n'))

Returns the number of lines in a text file, test.txt
:code:`open('data/test.txt', 'r').read()` gets us the text of the file, we get the line by using :code:`.split('\n')`,
which splits the text at every new line character :code:`\n` and returns a list. Calling :code:`len` on the lists gives us the count of lines.

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
:code:`re.sub` calls the method :code:`repl` at each encounter of a punctuation followed by a letter or a number as
specified by the regular expression :code:`'['+string.punctuation+'][a-zA-Z0-9]+'`. :code:`repl` add a space between
the punctuation and the letter/number and return it.


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
:code:`line.strip()` will remove leading and trailing whitespaces from the line.
If its an empty line :code:`line.strip()` will be an empty string.


delete trailing spaces
======================

.. code-block:: bash

    python -c "print(' trailing spaces will be removed.                        '.rstrip())"


:code:`.rstrip()` method is applied on strings to strip all the trailing whitespace on the right side of the string.


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
:code:`split('\n')` will return the file as a list where each item of the list is a line from file.
:code:`[:10]` will perform a slicing operation on the list to return elements from index 0 to 9.

To run it for arbitrary files


.. code-block:: bash

    $ python -c "import sys; open(sys.argv[1], 'r').read().split('\n')[:10]" data/test.txt


last ten lines of file
======================

.. code-block:: python

    open('data/100west.txt', 'r').read().split('\n')[-10:]

Returns last 10 lines of a file
:code:`split('\n')` will return the file as a list where each item of the list is a line from file.
:code:`[-10:]` will perform a slicing operation on the list. Negative indexing, :code:`[-n]`, denotes nth element from the last.
Here, the slicing operation will return last 10 items of the list i.e. last 10 lines of the file.

To run it for arbitrary files


.. code-block:: bash

    $ python -c "import sys; open(sys.argv, 'r').read().split('\n')[-10:]" data/test.txt

Reverse a file line by line
===================================

.. code-block:: bash

    python -c "import sys;c=open('reverse.txt','w');c.write('\n'.join([x for x in open(sys.argv[1], 'r').read().split('\n')[::-1]]));c.close()" data/100west.txt

Creates a file with line in reverse order from that of the input file.

:code:`split('\n')` will return the file as a list where each item of the list is a line from file.
:code:`[::-1]` will reverse the list.


Get alternate lines from files starting from the top
======================================================

.. code-block:: bash

    python -c "import sys;c=open('alternate.txt','w');c.write('\n'.join([x for x in open(sys.argv[1], 'r').read().split('\n')[::2]]));c.close()" data/100west.txt

Creates a new file with alternate lines of the input file.
Here, slicing operation, :code:`[::2]`, is defined with a step=2. Which will extract every 2nd item of the list.
Thus, creating a list of every alternate line from a file.


Find the most common words in a file
======================================

.. code-block:: bash

    python -c "import string,collections,sys,re;z=re.sub('[\n{}]'.format(string.punctuation), '',  open(sys.argv[1],'r').read().lower());x=collections.Counter(z.split(' '));del x[''];print(sorted(x.items(), key=lambda kv: kv[1], reverse=True)[:15])"

Returns the 15 most used words in a text file.
:code:`re.sub('[\n{}]'.format(string.punctuation), '',  open(sys.argv[1],'r').read().lower())` this code will strip all the
punctuations and newline characters from the text and :code:`.lower()` will convert the text into lowercase.

:code:`z.split(' ')` will return a list of all the words in the given file.

:code:`collections.Counter` will take the list and creates a list of dictionary as :code:`[{<item>: <frequency of item in the list>}, ...]`

The list of dictionary will be sorted by value with :code:`sorted(x.items(), key=lambda kv: kv[1], reverse=True)` and slicing :code:`[:15]`
will return top most common words in the file.


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
