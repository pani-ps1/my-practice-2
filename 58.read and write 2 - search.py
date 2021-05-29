# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 03:16:14 2020

@author: utob
"""
# esme_file = 'data/000.txt'
# with open (esme_file) as f:
#     for khat in f :
#         print(khat)
        
esme_file = 'data/000.txt'
with open (esme_file) as f:
    khotut = f.readlines()
    
for khat in khotut:
    print(khat)