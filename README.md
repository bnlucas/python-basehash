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

base62 = basehash.base62()

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

base62 = basehash.base62()

hashed   = base62.hash(2013, 8)
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

base62 = base62(1.75) # base62(generator=1.75)
```

Maximum number while hashing
----------------------------
There is a maximum number while hashing with any given base. To find out what
this number is, we use the `Base^Length - 1`.

```python
import basehash

base36 = basehash.base36()

print base36.maximum_value(12) # or base36.maximum(length)
```
```
4738381338321616895
```

So with the max number for `base36` at length `12` as `4738381338321616895` we
get the following:

```python
import basehash

base36 = basehash.base36()

hash = base36.hash(4738381338321616895, 12)
# 'DR10828P4CZP'

hash = base36.hash(4738381338321616896, 12)
# ValueError: Number is too large for given length. Maximum is 36^12 - 1.
```

Extending
---------
Extending is made easy with some time spent determining the next highest prime
dynamically, the fastest possible that I have been able to make it so far.

```python
import basehash

custom = basehash('24680ACEGIKMOQSUWYbdfhjlnprtvxz')

print custom.encode(2013)       # 66x
print custom.decode('66x')      # 2013
print custom.hash(2013, 8)      # 8AQAQdYd
print custom.unhash('8AQAQdYd') # 2013
print custom.maximum_value(12)  # 787662783788549760
```

[pc]: https://github.com/KevBurnsJr/pseudocrypt
[kb]: https://github.com/KevBurnsJr
[bp]: http://en.wikipedia.org/wiki/Baillie-PSW_primality_test
