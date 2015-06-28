import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import basehash


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


if sys.argv[-1] == 'prep':
    os.system('python setup.py sdist')
    sys.exit()


setup(
    name='BaseHash',
    version=basehash.__version__,
    description='Reversible obfuscated identifier hashes.',
    long_description='''
BaseHash is a small library for creating reversible obfuscated identifier hashes
to a given base and length. The project is based on the GO library, PseudoCrypt
by Kevin Burns (https://github.com/KevBurnsJr/pseudocrypt). The library is 
extendible to use custom alphabets and other bases.

The library uses golden primes and the Baillie-PSW primality test or the
`gmpy2.is_prime` (if available) for hashing to maximum value base ** length - 1.
    ''',
    author='Nathan Lucas',
    author_email='bnlucas@outlook.com',
    url='http://bnlucas.github.io/python-basehash',
    download_url='https://github.com/bnlucas/python-basehash/archive/master.zip',
    packages=['basehash'],
    package_data={'': ['LICENSE'], 'tests': '*.py'},
    package_dir={'basehash': 'basehash'},
    include_package_data=True,
    install_requires=[],
    license=open('LICENSE').read(),
    zip_safe=False,
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
)
