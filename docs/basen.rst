Built-in ``BaseN``
==================

BaseHash comes with a few built-in bases, ``Base36``, ``Base52``, ``Base56``,
``Base58``, ``Base62``, and ``Base94``.


BaseN.BASEN
-----------

| ``BASE36`` = ``0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ``
| ``BASE52`` = ``0123456789BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz``
| ``BASE56`` = ``23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz``
| ``BASE58`` = ``123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz``
| ``BASE62`` = ``0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz``
| ``BASE94`` = ``!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~``


encode
------

.. py:function:: baseN.encode(num)

   Encodes *int* ``num`` to ``baseN``. Returns ``base_encode(num, BASEN)``.
   Returns ``string``


decode
------

.. py:function:: baseN.decode(key)

   Decodes *string* key from ``baseN``. Returns ``base_decode(key, BASEN)``.
   Returns ``int``


hash
----

.. py:function:: baseN.hash(num[, length=HASH_LENGTH])

   Hashes *int* ``num`` to ``baseN`` at *int* ``length`` characters. Returns
   ``base_hash(num, length, BASEN)``.
   Returns ``string``


unhash
------

.. py:function:: baseN.unhash(key)

   Unhashes *string* ``key`` from ``baseN``. Returns ``base_unhash(key, BASEN)``.
   Returns ``int``


maximum
-------

.. py:function:: baseN.maximum([length=HASH_LENGTH])

   Returns maximum value for a hash of given *int* ``length``. Returns
   ``base_maximum(len(BASEN), length)``
   Returns ``int``
