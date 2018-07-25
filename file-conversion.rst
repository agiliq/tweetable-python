file conversions
===================

csv to json

json to csv

csv to sqlite

base64 encoding

base64 decoding

zip all .txt files in directory
===============================

.. code-block:: python

    import zipfile, os; myzip = zipfile.ZipFile('test.zip', 'w'); [myzip.write(each) for each in os.listdir() if each.endswith('.txt')]

Creates a zip file called test.zip of all the .txt files present in your current directory.
zipfile.ZipFile creates a new zip file. os.listdir() lists all the files in the current directory.


batch rename files in directory

prettify json
=============

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