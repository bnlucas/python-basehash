import os
import sys
import setuptools

exec(open('basehash/version.py').read())

with open('README.md', 'r') as f:
    long_description = f.read()

license_text = '''
Copyright 2013-2019 Nathan Lucas

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

setuptools.setup(
    name='BaseHash',
    version=__version__,
    author='Nathan Lucas',
    author_email='bnlucas@outlook.com',
    description='Reversible obfuscated identifier hashes.',
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='http://bnlucas.github.io/python-basehash',
    packages=['basehash'],
    package_data={'': ['LICENSE'], 'tests': ['*.py']},
    package_dir={'basehash': 'basehash'},
    include_package_data=True,
    install_requires=['six'],
    license=license_text,
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
