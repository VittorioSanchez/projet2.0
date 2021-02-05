# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 18:35:58 2016

@author: Florian
"""
import bd
pseudo=input('Insérer le pseudo : ')
bd.LecturebdPseudo(pseudo)
score=input('Insérer le score : ')
pays=input('Insérer le pays : ')
bd.Ecriturebd(pseudo, score, pays)