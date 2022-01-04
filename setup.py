#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Installation du programme d'inventaire pour Polytechnique.

Created on Tue Jan  4 09:14:49 2022

@author: emilejetzer
"""

import platform

from setuptools import setup

mainscript = 'inventaire.py'

if platform.system() == 'Windows':
    setup(app=[mainscript], setup_requires=['py2exe'])
elif platform.system() == 'Darwin':
    setup(app=[mainscript], setup_requires=['py2app'])
