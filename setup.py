# -*- coding: utf-8 -*-
# Copyright (c) 2012 Infrae. All rights reserved.x

from setuptools import setup, find_packages
import os

version = '1.0dev'

setup(name='smitheme.blues',
      version=version,
      description="Alternate SMI Skin for Silva 3.0",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='skin silva smi',
      author='Infrae',
      author_email='info@infrae.com',
      url='http://infrae.com/products/silva',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['smitheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      )
