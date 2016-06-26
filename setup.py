#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=2 et sw=2 sts=2
#
# Copyright © 2016 Mohammad Amin Sameti <mamins1376@gmail.com>
#
# Distributed under terms of the GNU General Public License v3 license.

"""
setup for Subscene
"""

from setuptools import setup, find_packages

description = readme = 'python wrapper for Subscene subtitle database.'
try:
  with open('README','r') as f:
    readme = f.read()
except Exception:
  pass

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(
  name='subscene',
  version='1.0.0',
  description=description,
  long_description=readme,
  author='Mohammad Amin Sameti',
  author_email='mamins1376@gmail.com',
  url='https://github.com/mamins1376/Subscene-API',
  license='GNU General Public License v3 or later',
  keywords = 'subscene api wrapper python3',
  install_requires=requirements,
  packages=find_packages(),
  classifiers = [
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Topic :: Software Development',
    'Topic :: Internet :: WWW/HTTP',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',
    'Development Status :: 5 - Production/Stable'
    ]
)

