#!/usr/bin/env python
from setuptools import setup, find_packages
setup(
    name = "pyfunhtml",
    version = "0.1",
    packages = find_packages(),

    # metadata for upload to PyPI
    author = "Evan McClanahan",
    author_email = "mcclanahan@gmail.com",
    description = "Functional HTML generation DSL library.",
    license = "PSF",
    keywords = "HTML generation",
    url = "http://github.com/evanmcc/pfh",
)
