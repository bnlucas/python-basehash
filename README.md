# BaseHash

[![Build Status](https://travis-ci.org/bnlucas/python-basehash.png?branch=master)](https://travis-ci.org/bnlucas/python-basehash)

# *** DEPRECATED ***
BaseHash is now deprecated and will no longer be maintained.
[Obfuskey](https://github.com/bnlucas/obfuskey) has been created to replace it. A
decision made when looking to modernize this utility. Obfuskey is only tested on
python3.6 and higher, so if you're needing lower support, you can continue to use
BaseHash.

BaseHash is a small library for creating reversible obfuscated identifier hashes
to a given base and length. The project is based on the GO library, [PseudoCrypt][pc]
by [Kevin Burns][kb]. The library is extendible to use custom alphabets and other
bases.

The library uses golden primes and the [Baillie-PSW][bp] primality test or the
`gmpy2.is_prime` (if available) for hashing to `maximum` length (`base ** length - 1`).

## v3.0.5

A massive overhaul was done with the primality algorithms. Including support for
[gmpy2][gmp] if it available on the system for that much more of an increase.

All methods being used to check primality in `primes.py` have been optimized and
benchmarked to try to get the best possible preformance when `gmpy2.is_prime`
and `gmpy2.next_prime` are not available.


## Install

```
pip install basehash
```

## Testing

```
nosetests tests/
```

[pc]: https://github.com/KevBurnsJr/pseudocrypt
[kb]: https://github.com/KevBurnsJr
[bp]: http://en.wikipedia.org/wiki/Baillie-PSW_primality_test
[gmp]: https://gmpy2.readthedocs.org/
