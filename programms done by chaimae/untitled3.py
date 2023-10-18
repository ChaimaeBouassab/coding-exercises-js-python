# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 12:36:48 2023

@author: pc
"""
import math
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
class cercle:
    def __init__(self,o,r):'''o est un point de coordonnees x et y'''
          
        self.o=o
        self.r=r
    def surface(self):
        return pi*(self.r)**2
    
    def perimetre(self):
        return 2*pi*self.r
    def distance(self,p):'''calculer distance entre deux points'''
    d=math.sqrt((self.x-p.x)**2+(self.y-p.y)**2)
    return p
    def testappartenance(self): 
        d=self.o.distance(p)
        if d-self.r==0:
            print('appartient')
        else:
            print('nooon')

            
