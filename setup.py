#!/usr/bin/env python

from os.path import join, dirname
from distutils.core import setup

packages = [
    'pygephi'
]

setup(name='pygephi',
      version="1.0",
      description='Python scripts that can be used to stream data to gephi',
      long_description=open(join(dirname(__file__), 'README'), 'r').read(),
      author='Andre Panisson',
      author_email='panisson@gmail.com',
      license='Apache 2.0',
      url='https://github.com/panisson/pygephi_graphstreaming',
      packages=packages,
      classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization'
      ]
)
