# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:33:04 2020

@author: utob
"""
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "smile",
        ":(": "cry"        
        }
    output=""
    for word in words:
        output +=emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))
