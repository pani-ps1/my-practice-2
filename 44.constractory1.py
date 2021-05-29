# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 15:47:36 2020

@author: utob
"""

class Person:
    def __init__(self,name):
        self.name = name
        
    def talk(self):
        print(f"hi, i am {self.name}")
        
        
john = Person("john smith")
john.talk()

bob = Person("bob smith")
bob.talk()
        