Date and Calendar
+++++++++++++++++++++++

Display current year's calendar
-----------------------------------

.. code-block:: bash

    python -c "import calendar, datetime; today = datetime.datetime.today();print(calendar.TextCalendar().formatyear(today.year))"

Generates the calendar for current year using python's :code:`calendar` module. :code:`datetime.datetime.today()` returns
today's date and time.


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

Similar to generating the year's calendar for the current month by passing the current month along with the year as
parameters.


Number of days remaining to Christmas
--------------------------------------

.. code-block:: bash

    python -c "import datetime; print('{} day(s)'.format((datetime.date(year=datetime.datetime.now().year, month=12, day=25) - datetime.datetime.now().date()).days))"

This will return the number of days till Christmas. Python's :code:`-` operator returns the difference between dates.


Is the current year a leap year?
---------------------------------

.. code-block:: bash

    python -c "import calendar, datetime; print(calendar.isleap(datetime.datetime.now().year))"

Python's :code:`calendar` module has a method :code:`isleap()` which returns boolean value depending on whether
current year is leap year or not.


Unix epoch time
-----------------------------

.. code-block:: bash

    python -c "import datetime; print('{} seconds since the epoch'.format(datetime.datetime.now().timestamp()))"

Unix epoch time is the time, in seconds, since 1 Jan 1970. Above code will return unix epoch time since 1 Jan 1970 till now.
