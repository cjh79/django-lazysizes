#!/usr/bin/env python
from setuptools import setup, find_packages

from lazysizes import __version__ as version

setup(
    name="Django-LazySizes",
    version=version,
    author="Chris Hawes",
    author_email="chrishawes@gmail.com",
    description="Tools for using lazysizes.js with Django templates.",
    license="BSD",
    packages=find_packages(),
    test_suite='testrunner.run_tests',
    install_requires=["django >= 1.11", "beautifulsoup4 >= 4.5.3", "lxml"],
)
