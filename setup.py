#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=2 et sw=2 sts=2

# This file is part of Subscene-API.
#
# Subscene-API is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Subscene-API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
setup for Subscene
"""

from setuptools import setup, find_packages

description = readme = 'python wrapper for Subscene subtitle database.'
requirements = []
try:
  with open('README','r') as f:
    readme = f.read()
  with open('requirements.txt') as f:
    requirements = f.read().splitlines()
except Exception:
  pass

setup(
  name='subscene-api',
  version='1.0.0',
  description=description,
  long_description=readme,
  author='Mohammad Amin Sameti',
  author_email='mamins1376@gmail.com',
  url='https://github.com/mamins1376/Subscene-API',
  license='GNU General Public License v3 or later',
  keywords = 'subscene api wrapper python3',
  install_requires=requirements,
  packages=['subscene'],
  classifiers = [
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Topic :: Software Development',
    'Topic :: Internet :: WWW/HTTP',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',
    'Development Status :: 5 - Production/Stable'
    ]
)

