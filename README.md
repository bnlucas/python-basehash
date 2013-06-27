BaseHash
========

BaseHash is a small library for creating reversible obfuscated identifier hashes
to a given base and length. The project is based on the GO library, [PseudoCrypt][pc]
by [Kevin Burns][kb]. The library is extendible to use custom alphabets and other
bases.

The library uses golden primes and the [Baillie-PSW][bp] primality test for hashing 
to `n` length. From testing, I have gotten `base62` up to `171` in length.

```
Maximum number is Base^Length - 1.
-> 62^171 - 1 or 315485137315301582773830923281251564555089304044116975095028710
				 008180170985809814948409129256031320171601473029340987051144213
				 425607224233134700199050224309707192084206558324823774511143549
				 765069844412467187455459156942237963528166277256376429656681225
				 8180788198965409784329587392583208081351811265973977087
```

Encode
------
```python
from basehash import base62

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
from basehash import base62

hashed   = base62.hash(2013, 8)
unhashed = base62.unhash('6LhOma5b')

print hashed, unhashed
```
```
6LhOma5b 2013
```

Generating your own primes
--------------------------
The default primes are generated using the golden ratio, `1.618033988749894848`
but this can be changed with `basehash.base.GENERATOR`

```python
# Generate primes, default golden ratio.
GENERATOR = 1.618033988749894848 # Change to whatever you'd like
```

Maximum number while hashing
----------------------------
There is a maximum number while hashing with any given base. To find out what
this number is, we use the `Base^Length - 1` inside the `base_maximum(length)`
method

```python
from basehash import base36

print base36.maximum(12)
```
```
4738381338321616895
```

So with the max number for `base36` at length `12` as `4738381338321616895` we
get the following:

```python
from basehash import base36

hash = base36.hash(4738381338321616895, 12)
# 'DR10828P4CZP'

hash = base36.hash(4738381338321616896, 12)
# ValueError: Number is too large for given length. Maximum is 36^12 - 1.
```

Extending
---------

```python
from basehash.base import *

ALPHA = tuple('24680ACEGIKMOQSUWYbdfhjlnprtvxz')

# Length 'base' is 31 -> len(ALPHA)

def encode(num):
	return base_encode(num, ALPHA)

def decode(key):
	return base_decode(key, ALPHA)

def hash(num, length=HASH_LENGTH):
	return base_hash(num, length, ALPHA)

def unhash(key):
	return base_unhash(key, ALPHA)

def maximum(length=HASH_LENGTH):
	return base_maximum(len(ALPHA), length)
```

[pc]: https://github.com/KevBurnsJr/pseudocrypt
[kb]: https://github.com/KevBurnsJr
[bp]: http://en.wikipedia.org/wiki/Baillie-PSW_primality_test
