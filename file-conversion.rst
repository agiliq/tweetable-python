file conversions
----------------

csv to json
===========

.. code-block:: python

    import csv,json;reader = csv.DictReader(open('data/xyz.csv', 'r'), fieldnames=( "User","Country","Age"))
    out=open('data/out.json','w'); out.write(json.dumps([row for row in reader]))

Converts a given file of comma separated values to json and store it in another file.
The csv used here doensnt' contain headers for the columns.


json to csv
===========

.. code-block:: python

    import json, csv; _json=json.loads(open('data/out.json', 'r').read())
    out=open('data/converted.csv', 'w')
    [out.write(','.join([x[x.keys()[i]] for i in range(len(x))]) + '\n')  for x in _json]

Creates a csv file from a json file.


csv to sqlite
=============


base64 encoding
===============

.. code-block:: python

    base64.encode(open('data/100west.txt', 'r'), open('data/encoded.txt', 'w'))

Converts an input file to base64 encoded file.


base64 decoding
===============

.. code-block:: python

    base64.decode(open('data/encoded.txt', 'r'), open('data/decoded.txt', 'w'))

Decodes the base64 encoded file back to its original encoding.


zip all .txt files in directory
===============================

.. code-block:: python

    import zipfile, os; myzip = zipfile.ZipFile('test.zip', 'w'); [myzip.write(each) for each in os.listdir() if each.endswith('.txt')]

Creates a zip file called test.zip of all the .txt files present in your current directory.
zipfile.ZipFile creates a new zip file. os.listdir() lists all the files in the current directory.


batch rename files in directory
===============================


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
