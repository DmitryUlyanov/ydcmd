#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='ydcmd',
      version='1.0',
      packages=['ydcmd'],
      package_dir={'ydcmd': 'ydcmd'},
      # package_data={
      #   'raw2png': ['script/jsx/*', 'script/*.js'],
      #   },
      entry_points = {'console_scripts' : ['ydcmd = ydcmd.ydcmd:main']},
      #install_requires = ['lxml==4.2.4'],
      # scripts = [
      #   'ydcmd.py'
      # ]
     )