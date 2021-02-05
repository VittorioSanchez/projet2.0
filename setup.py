# -*- coding: utf-8 -*-
"""
Created on Wed May 11 15:30:23 2016

Author: Florian
"""

from cx_Freeze import setup, Executable
setup(
    name='projet',
    version='1',
    description='jeu projet',
    executables=[Executable('projet6.py')],

)