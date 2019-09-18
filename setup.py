import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

exec(open('basehash/version.py').read())

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


if sys.argv[-1] == 'prep':
    os.system('python setup.py sdist')
    sys.exit()


setup(
    name='BaseHash',
    version=__version__,
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
    package_data={'': ['LICENSE'], 'tests': ['*.py']},
    package_dir={'basehash': 'basehash'},
    include_package_data=True,
    install_requires=['six'],
    license='''
Copyright 2013 Nathan Lucas

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
    ''',
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
