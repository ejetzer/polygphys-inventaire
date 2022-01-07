#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inventaire.

Created on Tue Jan  4 09:18:43 2022

@author: emilejetzer
"""

import platform

from polygphys.inventaire import main
from polygphys.outils.config import FichierConfig
from pathlib import Path

CHEMINS = {'Darwin': Path('/Volumes/GeniePhysique/Techniciens/'),
           'Windows': Path('Z:/'),
           None: Path('~/.inventaire').expanduser().resolve()}
SOUS_CHEMIN = Path('Emile_Jetzer/Inventaire/')

if __name__ == '__main__':
    dossier = CHEMINS.get(platform.system(), CHEMINS[None]) / SOUS_CHEMIN
    cfg = dossier / 'default.cfg'

    if not dossier.exists():
        dossier.mkdir()
        macos_db = CHEMINS['Darwin'] / SOUS_CHEMIN / 'inventaire.sqlite'
        win_db = CHEMINS['Windows'] / SOUS_CHEMIN / 'inventaire.sqlite'
        win_db = win_db.lstrip('\\').lstrip('/')

        with cfg.open('w') as f:
            f.write(f'''[bd]
    Darwin: sqlite:///{macos_db}
    Windows: sqlite:///{win_db}
    tables:
        boites
        inventaire
    formulaires:
        boites
        inventaire

[tkinter]
    title: Inventaire du département de génie physique à Polytechnique Montréal
''')

        db.touch()

    f = FichierConfig(cfg)
    f.set('bd', 'adresse', f.geturl('bd', platform.system()).replace('\\', '/'))
    
    main(dossier)
