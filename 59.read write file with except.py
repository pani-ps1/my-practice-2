# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 02:52:29 2020

@author: utob
"""

esme_file = 'data/0002w.txt'

try:
    with open (esme_file) as f:
        mohtaviat = f.read()
except FileNotFoundError :
    print('file vojud nadarad')
else:
    kalamat = mohtaviat.split()
    tedad_kalamat = len(kalamat)
    print(f'file {esme_file} daraye {tedad_kalamat} kalame mibashad')
    