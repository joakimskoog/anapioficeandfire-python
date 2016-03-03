#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'ujson==1.35', 'requests==2.9.1', 'six==1.10.0'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='anapioficeandfire',
    version='0.1.1',
    description="A Python helper library for anapioficeandfire.com",
    long_description=readme + '\n\n' + history,
    author="Joakim Skoog",
    author_email='joakimskooog@gmail.com',
    url='https://github.com/joakimskoog/anapioficeandfire-python',
    packages=[
        'anapioficeandfire',
    ],
    package_dir={'anapioficeandfire':
                 'anapioficeandfire'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='anapioficeandfire',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
