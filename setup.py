#!/usr/bin/env python

from setuptools import setup

setup(
    name='mass',
    version='0.1.0',
    description='Merge and Simplify Scripts',
    long_description='automated tool for managing, combining and minifying javascript assets for web projects.',
    author='jack boberg alex padgett',
    author_email='info@codedbyhand.com',
    url='https://github.com/coded-by-hand/mass',
    license='BSD License',
    platforms=['Mac OSX'],
    packages=['mass'],
    install_requires=['distribute','jsmin','macfsevents'],
    zip_safe = False,
    entry_points = {
        'console_scripts': [
            "mass = mass.monitor:main"
        ],
    }
)
