Date and Calendar
+++++++++++++++++++++++

Display current year's calendar
-----------------------------------

.. code-block:: bash

    python -c "import calendar, datetime; today = datetime.datetime.today();print(calendar.TextCalendar().formatyear(today.year))"


Display current month's calendar
------------------------------------
.. code-block:: bash

    $ python -c "import calendar, datetime; today = datetime.datetime.today();print(calendar.TextCalendar().formatmonth(today.year, today.month))"
        July 2018
    Mo Tu We Th Fr Sa Su
                    1
    2  3  4  5  6  7  8
    9 10 11 12 13 14 15
    16 17 18 19 20 21 22
    23 24 25 26 27 28 29
    30 31


Number of days remaining to Christmas
--------------------------------------

.. code-block:: bash

    python -c "import datetime; print('{} day(s)'.format((datetime.date(year=datetime.datetime.now().year, month=12, day=25) - datetime.datetime.now().date()).days))"


Is the current year a leap year?
---------------------------------

.. code-block:: bash

    python -c "import calendar, datetime; print(calendar.isleap(datetime.datetime.now().year))"


Unix epoch time
-----------------------------

.. code-block:: bash

    python -c "import datetime; print('{} seconds since the epoch'.format(datetime.datetime.now().timestamp()))"
