BaseHash
========

[![Build Status](https://travis-ci.org/bnlucas/python-basehash.png?branch=master)](https://travis-ci.org/bnlucas/python-basehash)

BaseHash is a small library for creating reversible obfuscated identifier hashes
to a given base and length. The project is based on the GO library, [PseudoCrypt][pc]
by [Kevin Burns][kb]. The library is extendible to use custom alphabets and other
bases.

The library uses golden primes and the [Baillie-PSW][bp] primality test or the
`gmpy2.is_prime` (if available) for hashing to `maximum` length (`base ** length - 1`).

v3.3.0
------
A massive overhaul was done with the primality algorithms. Including support for
[gmpy2][gmp] if it available on the system for that much more of an increase.

All methods being used to check primality in `primes.py` have been optimized and
benchmarked to try to get the best possible preformance when `gmpy2.is_prime`
and `gmpy2.next_prime` are not available.

v3.0.0 vs v2.2.0 without gmpy2
------------------------------
```
--------------------------------------------------------------------------------
 basehash 3.0.0 vs basehash 2.2.1 speed comparison. (without gmpy2)
 testing against random 128-bit integer with BASE62 and length of 30.

 comparing best 100 of 1000 loops.
--------------------------------------------------------------------------------
 bh300                                                    @        0.011989977s 
 bh220                                                    @        0.019100001s 
--------------------------------------------------------------------------------
```

v3.0.0 vs v2.2.0 with gmpy2
---------------------------
```
--------------------------------------------------------------------------------
 basehash 3.0.0 vs basehash 2.2.1 speed comparison. (with gmpy2)
 testing against random 128-bit integer with BASE62 and length of 30.

 comparing best 100 of 1000 loops.
--------------------------------------------------------------------------------
 bh300                                                    @        0.002969882s 
 bh220                                                    @        0.018960006s 
--------------------------------------------------------------------------------
```

Install
-------

```
pip install basehash
```

Testing
-------

```
nosetests tests/
```

Encode
------
```python
import basehash

base62 = basehash.base62(8)

encoded = base62.encode(2013)
decoded = base62.decode('WT')

print encoded, decoded
```
```
WT 2013
```

Hash
----
```python
import basehash

base62 = basehash.base62(8)

hashed   = base62.hash(2013)
unhashed = base62.unhash('6LhOma5b')

print hashed, unhashed
```
```
6LhOma5b 2013
```

Generating your own primes
--------------------------
The `GENERATOR` variable uses the golden ratio, `1.618033988749894848`, to get
the next highest prime of `base ** number * generator`. This can be overridden
within the base classes.

```python
import basehash

base62 = basehash.base62(generator=1.75)
```

Maximum number while hashing
----------------------------
There is a maximum number while hashing with any given base. To find out what
this number is, we use the `Base^Length - 1`.

```python
import basehash

base36 = basehash.base36(10)

print base36.maximum
```
```
4738381338321616895
```

So with the max number for `base36` at length `12` as `4738381338321616895` we
get the following:

```python
import basehash

base36 = basehash.base36(12)

hash = base36.hash(4738381338321616895)
# 'DR10828P4CZP'

hash = base36.hash(4738381338321616896)
# ValueError: Number is too large for given length. Maximum is 36^12 - 1.
```

Extending
---------
Extending is made easy with some time spent determining the next highest prime
dynamically, the fastest possible that I have been able to make it so far.

```python
import basehash

custom = basehash.base('24680ACEGIKMOQSUWYbdfhjlnprtvxz', 8)

print custom.encode(2013)       # 66x
print custom.decode('66x')      # 2013
print custom.hash(2013)      # 8AQAQdYd
print custom.unhash('8AQAQdYd') # 2013
print custom.maximum         # 787662783788549760
```

[pc]: https://github.com/KevBurnsJr/pseudocrypt
[kb]: https://github.com/KevBurnsJr
[bp]: http://en.wikipedia.org/wiki/Baillie-PSW_primality_test
[gmp]: https://gmpy2.readthedocs.org/


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/bnlucas/python-basehash/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

