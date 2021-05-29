# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:27:27 2020

@author: utob
"""

class Point:
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        

Point1 = Point()
Point1.x = 10
Point1.y = 20
print(Point1.x)
Point1.draw()

Point2 = Point()
Point2.x = 1 
print(Point2.x)
