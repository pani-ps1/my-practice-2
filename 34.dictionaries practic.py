# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:21:48 2020

@author: utob
"""

phone = input("phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
    }
output = ""
for ch in phone:
    output += digits_mapping.get(ch,"!") + " "
print(output)    


#chera ! be akhar javab ezafe nemikone?