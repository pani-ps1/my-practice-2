# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:36:05 2020

@author: utob
"""

message = input(">")
words = message.split(' ')
emojis = {
     ":)": "smile",
     ":(": "cry",
     }
output =""
for word in words:
    output += emojis.get(word, word) +" "
print(output)