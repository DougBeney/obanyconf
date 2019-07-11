#!/usr/bin/env python3

from distutils.core import setup
import time

setup(
  name='''obanyconf''',
  version=time.strftime('%Y.%m.%d.%H.%M.%S', time.gmtime(1551526611)),
  description='''A script to use any configuration file type to configure openbox.''',
  author='''Doug Beney''',
  author_email='''contact@dougie.io''',
  url='''https://github.com/DougBeney/obanyconf''',
  py_modules=['''obanyconf'''],
  install_requires=[
    'anymarkup',
  ]
)
