#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Installation du programme d'inventaire pour Polytechnique.

Created on Tue Jan  4 09:14:49 2022

@author: emilejetzer
"""

import platform

from setuptools import setup

if platform.system() == 'Windows':
    setup_requires = ['py2exe']
elif platform.system() == 'Darwin':
    setup_requires = ['py2app']
else:
    setup_requires = []

setup(setup_requires=setup_requires)
