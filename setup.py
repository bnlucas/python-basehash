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
    long_description=open('README.md').read() + '\n\n' + open('HISTORY.md').read(),
    author='Nathan Lucas',
    author_email='nathan@bnlucas.com',
    url='http://bnlucas.github.io/python-basehash',
    download_url='https://github.com/bnlucas/python-basehash/archive/master.zip',
    packages=['basehash'],
    package_data={'': ['LICENSE'], 'tests': '*.py'},
    package_dir={'basehash': 'basehash'},
    include_package_data=True,
    install_requires=['six'],
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
