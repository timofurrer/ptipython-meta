# -*- coding: utf-8 -*-

"""
    This is a meta package to make ptipython available as a package.
"""

from setuptools import setup


setup(
    name="ptipython",
    version="1.0.1",
    license="MIT",

    description="Metapackage to install ptpython and ipython.",

    author="Timo Furrer",
    author_email="tuxtimo@gmail.com",

    url="https://github.com/timofurrer/ptipython-meta",

    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",

    install_requires=[
        # Python 2.7
        "ipython<6; python_version=='2.7'",
        "ptpython<2; python_version=='2.7'",
        # Python 3.4
        "ipython<7; python_version=='3.4'",
        "ptpython<2; python_version=='3.4'",
        # Python 3.5+
        "ipython; python_version>='3.5'",
        "ptpython; python_version>='3.5'",
    ],

    keywords=[
        "ptpython", "ipython", "ptipython",
        "metapackage", "pypi", "try"
    ]
)
