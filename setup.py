# -*- coding: utf-8 -*-

"""
    This is a meta package to make ptipython available as a package.
"""

from setuptools import setup


setup(
    name="ptipython",
    version="1.0.0",
    license="MIT",

    description="Metapackage to install ptpython and ipython.",

    author="Timo Furrer",
    author_email="tuxtimo@gmail.com",

    url="https://github.com/timofurrer/ptipython-meta",

    include_package_data=True,

    install_requires=[
        "ptpython",
        "ipython"
    ],

    keywords=[
        "ptpython", "ipython", "ptipython",
        "metapackage", "pypi", "try"
    ]
)
