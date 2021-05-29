# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 03:09:29 2020

@author: utob
"""

def shomareshe_tedade_kalamat(esme_file):
    try:
        with open(esme_file) as f :
            mohtaviat = f.read()
    except  FileNotFoundError:
        print('file moshakas shode vojud nadarad')
    else:
        kalamat = mohtaviat.split()
        tedad_kalamat = len(kalamat)
        print(f'file {esme_file} daaye {tedad_kalamat} kalame mbashad')

esme_file = 'data/0002w.txt'
shomareshe_tedade_kalamat(esme_file)