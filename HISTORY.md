1.0.7 (2013-07-06)
++++++++++++++++++

- There was an issue with hashes sometimes being returned one to two charcters
  shorter than `length`, causing `base.base_unhash` to not function properly. To
  fix this, the hashes are right-padded with `0`.

- Since `0` raises an error inside `primes.invmul`, `base.base_unhash` is unable
  to unhash it. To allow the start of your number sequence to be `0` instead of
  `1`, if needed, hashing `base.base_hash(0, length=6)` will return
  `''.rjust(length, alphabet[0])`.

1.0.6 (2013-06-29)
++++++++++++++++++

- Fixed issues with setup.py. First time using a setup.py within a package,
  first time publishing the library outside of GitHub.

1.0.5 (2013-06-28)
++++++++++++++++++

- Added nose unittests.

1.0.4 (2013-06-28)
++++++++++++++++++

- Added setup.py, LICENSE, HISTORY.rst, and .travis.yaml.

1.0.3 (2013-06-27)
++++++++++++++++++

- Added a simple test for `prime < 31` to reduce calculation time.

- Fixed issue of `strong_pseudoprime(n, 3)` giving false results.

1.0.2 (2013-06-27)
++++++++++++++++++

- Changed primality test from Miller-Rabin to Baillie-PSW. This algorithm is
  significantly faster.

- Changed determination to use `sqrt(n)` or `isqrt(n)` to an improved version of
  `isqrt(n)`.

- BaseHash is now PEP compliant.

1.0.1 (2013-06-25)
++++++++++++++++++

- Changed primality test from Fermat to Miller-Rabin. Improved accuracy on false
  results when it comes to pseudoprimes.

1.0.0 (2013-06-24)
++++++++++++++++++

- Released code to GitHub repository python-basehash
  https://github.com/bnlucas/python-basehash

0.0.1 (2013-06-23)
++++++++++++++++++

- Initialization
