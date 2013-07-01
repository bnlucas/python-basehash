The heart of BaseHash
=====================

BaseHash Constants
------------------

The two constants of BaseHash are ``HASH_LENGTH`` and ``GENERATOR``.

``HASH_LENGTH``, default set to ``6``, is used as a default hashing length,
which can be overridden in ``baseN.hash()``.

``GENERATOR`` uses the `Golden Ratio`_, ``1.618033988749894848``, to determine
the next highest prime, which is based on ``base ^ length - 1``. ``GENERATOR``
can either be overridden globally or can be overridden within ``base_hash`` or 
``base_unhash``.


prime
-----

.. py:function:: prime(base, n, gen)

   Returns next highest prime. using base^n * gen.


base_encode
-----------

.. py:function:: base_encode(num, alphabet)

   Encodes *int* ``num`` to *base* ``alphabet``.
   Returns ``string``


base_decode
-----------

.. py:function:: base_decode(key, alphabet)

   Decodes *string* ``key`` from *string* ``alphabet`` (or ``base``).
   Returns ``int``


base_hash
---------

.. py:function:: base_hash(num, length, alphabet[, gen=GENERATOR])

   Hashes *int* ``num`` to *string* ``alphabet`` (or ``base``), *int* ``length``
   digits long using the built in ``base.GENERATOR``, which can be overridden.
   Returns ``string``


base_unhash
-----------

.. py:function:: base_unhash(key, alphabet[, gen=GENERATOR])

   Unhashes *string* ``key`` from *string* ``alphabet`` (or ``base``) using the
   built in ``base.GENERATOR``, which can be overridden.


base_maximum
------------

-- py:function:: base_maximum(base, length)

   Returns maximum ``int`` that *int* ``base`` ^ *int* ``length`` can take.
   Returns ``int``


.. _Golden Ratio: http://en.wikipedia.org/wiki/Golden_ratio
