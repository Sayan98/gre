#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='gre',
    version='0.1',
    author="Sayan Goswami",
    author_email='<goswami.sayan47@gmail.com>',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gre=gre.main:cli
    ''',
)
