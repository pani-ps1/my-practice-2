# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 04:04:08 2020

@author: utob
"""

def shomareshe_tedade_kalamat(esme_file):
    try:
        with open(esme_file) as f :
            mohtaviat = f.read()
    except  FileNotFoundError:
        # print('file moshakas shode vojud nadarad')
        pass
    else:
        kalamat = mohtaviat.split()
        tedad_kalamat = len(kalamat)
        print(f'file {esme_file} daraye {tedad_kalamat} kalame mbashad')

esme_file = ['data/000.txt','data/0003w.txt','data/0002w.txt','data/data1.txt']
for esm in esme_file:
    shomareshe_tedade_kalamat(esm)