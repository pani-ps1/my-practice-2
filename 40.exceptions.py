# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:12:12 2020

@author: utob
"""

#errors
# zamen etminan baraye naterikidan barname

try:
    age = int(input('age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('age cannot be 0.')    
except ValueError:
    print('invalid value')
    