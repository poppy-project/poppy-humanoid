#!/usr/bin/env python

import re
import sys

from setuptools import setup, find_packages


def version():
    with open('poppy_humanoid/_version.py') as f:
        return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read()).group(1)


setup(name='poppy-humanoid',
      version=version(),
      packages=find_packages(),

      install_requires=['pypot >= 4.0.0'],

      include_package_data=True,
      exclude_package_data={'': ['README', '.gitignore']},

      zip_safe=False,

      author='Poppy Station',
      author_email='dev@poppy-station.org',
      description='Poppy Humanoid Software Library',
      url='https://poppy-project.org',
      license='GNU GENERAL PUBLIC LICENSE Version 3',

      )
