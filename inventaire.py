#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inventaire.

Created on Tue Jan  4 09:18:43 2022

@author: emilejetzer
"""

from pathlib import Path

from polygphys.inventaire import main

if __name__ == '__main__':
    main(Path('~/.inventaire').expanduser())
