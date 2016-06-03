#!/usr/bin/env python

import re
import sys

from setuptools import setup, find_packages


def version():
    with open('poppy_humanoid/_version.py') as f:
        return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read()).group(1)

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(name='poppy-humanoid',
      version=version(),
      packages=find_packages(),

      install_requires=['poppy-creature >= 1.8',
                        'pypot >= 2.11'],

      include_package_data=True,
      exclude_package_data={'': ['README', '.gitignore']},

      zip_safe=False,

      author='Pierre Rouanet, Matthieu Lapeyre',
      author_email='pierre.rouanet@gmail.com',
      description='Poppy Humanoid Software Library',
      url='https://github.com/poppy-project/poppy-creature',
      license='GNU GENERAL PUBLIC LICENSE Version 3',

      **extra
      )
