#!/usr/bin/env python
"""
Fondant
=======

Utility functions and classes for the Python programmers
"""
from setuptools import setup


setup (
    name = 'Fondant',
    version = '0.3.3',
    url = 'https://github.com/amirouche/Fondant',
    license = 'BSD',
    author = 'Amirouche Boubekki',
    author_email = 'amirouche.boubekki@gmail.com',
    description = 'Utility functions and classes for the Python',
    long_description = __doc__,
    keywords = 'utility',
    packages = ['fondant'],
    zip_safe=False,
    platforms='any',
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
)
