ester eggs
++++++++++

The world's smallest hello world program?
------------------------------------------

.. code-block:: python

    import __hello__


Or :code-block:`python -c 'import __hello__'`.


What would Guido do?
-------------------------

.. code-block:: python

    import this

The :code:`import this` is well known, but let's look at the source code.

.. code-block:: python

    s = """Gur Mra bs Clguba, ol Gvz Crgref

    Ornhgvshy vf orggre guna htyl.
    Rkcyvpvg vf orggre guna vzcyvpvg.
    Fvzcyr vf orggre guna pbzcyrk.
    Pbzcyrk vf orggre guna pbzcyvpngrq.
    Syng vf orggre guna arfgrq.
    Fcnefr vf orggre guna qrafr.
    Ernqnovyvgl pbhagf.
    Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
    Nygubhtu cenpgvpnyvgl orngf chevgl.
    Reebef fubhyq arire cnff fvyragyl.
    Hayrff rkcyvpvgyl fvyraprq.
    Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
    Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
    Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
    Abj vf orggre guna arire.
    Nygubhtu arire vf bsgra orggre guna *evtug* abj.
    Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
    Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
    Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)

    print("".join([d.get(c, c) for c in s]))

It doesn't contain the Zen of Python, but :code:`d[chr(i+c)] = chr((i+13) % 26 + c)` gives it away. It is the Zen of Python with a Rot13 transform.


Are we Java yet?
---------------------

.. code-block:: python

    >>> from __future__ import braces

    File "<stdin>", line 1
    SyntaxError: not a chance


How does this work? Look at :code:`__futures__.py`. You won't find any :code:`braces`.
This error gets propagated to :code:`parso/python/errors.py`, where we find:

.. code-block:: python


    @ErrorFinder.register_rule(type='import_from')
    class _FutureImportRule(SyntaxRule):
        message = "from __future__ imports must occur at the beginning of the file"

        def is_issue(self, node):
            if _is_future_import(node):
                if not _is_future_import_first(node):
                    return True

                for from_name, future_name in node.get_paths():
                    # ...
                    if name == 'braces':
                        self.add_issue(node, message = "not a chance")
                    # ...

I believe I can fly
----------------------

.. code-block:: python

    import antigravity

This takes you to https://xkcd.com/353/. Let's look at :code:`antigravity.py`.

.. code-block:: python

    import webbrowser
    import hashlib

    webbrowser.open("https://xkcd.com/353/")

    def geohash(latitude, longitude, datedow):
        '''Compute geohash() using the Munroe algorithm.
        # ...

:code:`webbrowser.open("https://xkcd.com/353/")` is what opens the web page. This is another example of how "batteries included" Python is. It even comes with and `Interfaces for launching and remotely controlling Web browsers`.
