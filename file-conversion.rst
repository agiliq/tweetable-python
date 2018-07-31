File conversions
----------------

csv to json
===========

.. code-block:: python

    import csv,json;reader = csv.DictReader(open('data/example.csv', 'r'), fieldnames=( "User","Country","Age"))
    out=open('data/out.json','w'); out.write(json.dumps([row for row in reader]))

Converts a given file of comma separated values to json and store it in another file.
The csv used here doesn't contain headers for the columns.

:code:`csv.DictReader(open('data/example.csv', 'r'), fieldnames=( "User","Country","Age"))` gets us the DictReader object from the csv file with three columns specified as fieldnames. :code:`json.dumps([row for row in reader])`, converts the json object to string for writing it in output file and :code:`out.write()` method writes the data into the file.

To run it for arbitrary files


.. code-block:: bash

    $ python -c "import csv,json,sys;reader = csv.DictReader(open(sys.argv[1], 'r'), fieldnames=( "User","Country","Age"));out=open('data/out.json','w'); out.write(json.dumps([row for row in reader]))" data/example.csv


json to csv
===========

.. code-block:: python

    import json, csv; _json=json.loads(open('data/example.json', 'r').read())
    out=open('data/converted.csv', 'w')
    [out.write(','.join([x[x.keys()[i]] for i in range(len(x))]) + '\n')  for x in _json]

Creates a csv file from a json file.

:code:`json.loads(open('data/example.json', 'r').read())` Creates a json object from json file.


csv to sqlite
=============


base64 encoding
===============

.. code-block:: python

    import base64;base64.encode(open('data/100west.txt', 'r'), open('data/encoded.txt', 'w'))

Converts an input file to base64 encoded file.

To run it for arbitrary files


.. code-block:: bash

    $ python -c "import base64,sys,sys;base64.encode(open(sys.argv[1], 'r'), open('data/encoded.txt', 'w'))" data/test.txt


base64 decoding
===============

.. code-block:: python

    import base64;base64.decode(open('data/encoded.txt', 'r'), open('data/decoded.txt', 'w'))

Decodes the base64 encoded file back to its original encoding.

To run it for arbitrary files


.. code-block:: bash

    $ python -c "import base64,sys;base64.decode(open(sys.argv[1], 'r'), open('data/decoded.txt', 'w'))" data/test.txt


zip all .txt files in directory
===============================

.. code-block:: python

    import zipfile, os; myzip = zipfile.ZipFile('test.zip', 'w'); [myzip.write(each) for each in os.listdir() if each.endswith('.txt')]

Creates a zip file called test.zip of all the .txt files present in your current directory.
zipfile.ZipFile creates a new zip file. :code:`os.listdir()` lists all the files in the current directory.

To run it for arbitrary directory. You must provide the absolute path to the directory


.. code-block:: bash

    $ python -c "import zipfile,os,sys; myzip=zipfile.ZipFile('test.zip', 'w'); [myzip.write(each) for each in os.listdir(sys.argv[1]) if each.endswith('.txt')]" /User/xyz/files/


batch rename files in directory
===============================

Change all files with :code:`.txt` extension to :code:`.rst`.

Rename all files in directory to add .bak extension
=====================================================

Copy all files with name :code:`filename.ext` to `filename.bak.ext`

Find all python files in directory which are less than 280 chars, excepting lines which start with a #
=======================================================================================================

Managing your downloads folder
==================================

When you download files, it generally goes :code:`~/Downloads`.
This folder grows and becomes unwieldy as time goes.

So to manage this, we will create a folder of format :code:`YYYY-MM` in the :code:`~/Downloads` folder
and move all files tothe correct folder.


prettify json
=============

.. code-block:: python

    import json; json.dumps([{"one":123,"two":455,"three":789}], indent=4)

Returns a prettified json string for the given json object. The above json object will be converted as below:

.. code-block:: python

    [
        {
            "one": 123,
            "two": 455,
            "three": 789
        }
    ]

convert CSV to sqlite
-------------------------
