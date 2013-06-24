BaseHash
========

BaseHash is a small library for creating reversible obfuscated identifier hashes
to a given base and length. The project is based on the GO library, [PseudoCrypt][pc]
by [Kevin Burns][kb]. The library is extendible to use custom alphabets and other
bases.

The library uses golden primes and [Fermat's little theorem][flt] for hashing to
`n` length. From testing, I have gotten `base62` up to `171` in length.

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

Extending
---------
```python
from basehash.base import *

ALPHA = tuple('24680ACEGIKMOQSUWYbdfhjlnprtvxz')

# Length 'base' is 31 -> len(ALPHA)

def encode(num):
	return base_encode(num, len(ALPHA), ALPHA)

def decode(key):
	return base_decode(key, len(ALPHA), ALPHA)

def hash(num, length=HASH_LENGTH):
	return base_hash(num, length, len(ALPHA), ALPHA)

def unhash(key):
	return base_unhash(key, len(ALPHA), ALPHA)

def maximum(length=HASH_LENGTH):
	return base_maximum(len(ALPHA), length)
```

[ps]: https://github.com/KevBurnsJr/pseudocrypt
[kb]: https://github.com/KevBurnsJr
[flt]: http://en.wikipedia.org/wiki/Fermat's_little_theorem