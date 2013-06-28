import os
import sys

from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


setup(
    name='BaseHash',
    packages=['basehash'],
    version='1.0.5',
    description='Reversible obfuscated identifier hashes to a given base and length.',
    author='Nathan Lucas',
    author_email='nathan@bnlucas.com',
    url='http://bnlucas.github.io/python-basehash',
    download_url='https://github.com/bnlucas/python-basehash/archive/master.zip',
    package_data={'': ['LICENSE', 'HISTORY.rst']},
    keywords=['base', 'encoding', 'hash', 'hashing', 'security'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    long_description='''
BaseHash - Reversible obfuscated identifier hashing.
----------------------------------------------------

BaseHash comes with multiple base hashing packages, and is also extendible. use
this package to quickly hash integers to a given base and length.

- Base36, Base52, Base56, Base58, Base62, Base94.
- Extend with ease.
- Relies on primes base^len, example: base62 hash, 6 digits, uses
  (62 ** 6) * 1.618033988749894848, finds next highest prime.
'''
)
