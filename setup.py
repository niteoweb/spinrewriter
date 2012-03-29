# -*- coding: utf-8 -*-
"""Installer for this package."""

from setuptools import setup
from setuptools import find_packages

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = read('src', 'spinrewriter', 'version.txt').strip()

setup(name='spinrewriter',
      version=version,
      description="https://github.com/niteoweb/spinrewriter",
      long_description=read('README.rst') +
                       read('docs', 'HISTORY.rst') +
                       read('docs', 'LICENSE.rst'),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        ],
      keywords='API spinner SpinRewriter',
      author='NiteoWeb Ltd.',
      author_email='info@niteoweb.com',
      url='http://www.niteoweb.com',
      license='BSD',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      test_suite='spinrewriter',
      install_requires=[
          # list project dependencies
          'setuptools',
      ],
      extras_require={
          # list libs needed for unittesting this project
          'test': [
              'mock',
              'unittest2',
          ],
          'deploy': [
              'zest.releaser',   # bin/longtest
              'jarn.mkrelease',  # bin/mkrelease
          ],
      },
      )