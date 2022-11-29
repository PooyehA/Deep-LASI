Installation
=====

.. _installation:

Deep-LASI is a MATLAB program that uses neural networks for automated data analysis from Python libraries.
In order to use an automated data analysis make sure you installed the required software packages below.

System compatibility
------------

Deep-Lasi is compatible with Windows and Mac OS, and has been extensively tested on Mac OS systems. 
So far, we have not tested Deep-Lasi as extensively on Windows. If you encounter any problem, please
get in touch with us on the *Issue forum*.

.. image:: mac.png
   : scale: 100%
   : alt: Mac Logo
   
.. image:: ../figures/logos/windows.png
   : scale: 100%
   : alt: Windows Logo

Installation
------------



To use Deep-LASI, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

