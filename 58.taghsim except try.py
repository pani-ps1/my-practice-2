# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 01:58:23 2020

@author: pan
"""

print('2 adad ra baraye taghsim vared konid')
print('ba vared kardam q az barname kharej shavid')

while True:
    adad_aval = input('\nadad aval: ')
    if adad_aval == 'q':
        break
    adad_dovom = input('\nadad dovom: ')
    if adad_dovom == 'q':
        break
    try:
        hasele_taghsim = int(adad_aval)/int(adad_dovom)
    except ZeroDivisionError:
        print('taghsim adad bar sefr emkan pazir nist.')
    else:    
        print(hasele_taghsim)    