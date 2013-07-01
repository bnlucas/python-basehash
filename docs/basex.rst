Extending to ``BaseX``
======================

Much work was put into generating prime numbers on the fly, allowing BaseHash to
be extended to ``BaseX`` with ease. To extend the library, you just need to
import ``basehash.base`` and call a few mthods.

.. code-block:: python

   from basehash.base import *

   # ALPHA must be a tuple
   ALPHA = tuple('24680ACEGIKMOQSUWYbdfhjlnprtvxz')


   # hash `num` to `ALPHA` at `length` characters
   def hash(num, length=HASH_LENGTH):
       return base_hash(num, length, ALPHA)


   # unhash `key` from `ALPHA`
   def unhash(key):
       return base_unhash(key, ALPHA)

   ## optional methods:


   # encode `num` to `ALPHA`
   def encode(num):
       return base_encode(num, ALPHA)


   # decode `key` from `ALPHA`
   def decode(key):
       return base_decode(key, ALPHA)


   # return maximum value for `hash` at `length`
   def maximum(length=HASH_LENGTH):
       return base_maximum(len(ALPHA), length)
