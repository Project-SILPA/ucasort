#!/usr/bin/env python

from setuptools import setup, find_packages

name = "sort"

setup(
    name = name,
    version = "0.2.1",
    url = "http://silpa.org.in/sort",
    license = "LGPL-3.0",
    description = "Sort words basded on linguistics",
    author = "Santhosh Thottingal",
    author_email = "santhosh.thottingal@gmail.com",
    long_description = """Sort words basded on linguistics""",
    packages = find_packages(),
    include_package_data = True,
    setup_requires = ['setuptools-git'],
    install_requires = ['setuptools'],
    zip_safe = False,
    )