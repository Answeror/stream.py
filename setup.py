#!/usr/bin/env python

#import os
#import sys
from setuptools import setup, find_packages


classifiers = """
Development Status :: 3 - Alpha
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Utilities
"""

__doc__ = """Streams are iterables with a pipelining mechanism to enable data-flow
programming and easy parallelization.

See the reference documentation at <http://www.trinhhaianh.com/stream.py>.

Articles written by the author about the module can be viewed at <http://blog.onideas.ws/tag/project:stream.py>.

The code repository is located at <http://github.com/aht/stream.py>.
"""

setup(
    name='stream',
    version='0.8.3dev',
    description='Lazily-evaluated, parallelizable pipeline.',
    long_description=__doc__,
    author='Anh Hai Trinh',
    author_email='moc.liamg@hnirt.iah.hna:otliam'[::-1],
    keywords='lazy iterator generator stream pipe parallellization data flow functional list processing',
    url='http://github.com/aht/stream.py',
    platforms=['any'],
    classifiers=filter(None, classifiers.split("\n")),
    #py_modules=['stream'],
    packages=find_packages(exclude=['ez_setup']),
    use_2to3=True,
    install_requires=['distribute'],
    test_suite='nose.collector'
)
