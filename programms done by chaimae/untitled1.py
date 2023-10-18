# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 10:26:32 2023

@author: CHAIMAE
"""

class Rectangle:
    def __init__(self,Longueur,Largeur):
        self.lo=Longueur
        self.la=Largeur
    def perimetre(self):
        return (self.la + self.lo)*2
    def surface(self):
        return (self.la * self.lo)

class parallelepipede(Rectangle):
    def __init__(self,hauteur,Longueur,Largeur):
        super().__init__(Longueur, Largeur)
        self.h=hauteur
    def volume(self):
        return (self.h * self.lo * self.la)

    
    
    
Rectangle1=Rectangle(2, 3)
para=parallelepipede(4, 2, 3)
print('le perimetre est ',Rectangle1.perimetre())
print('la surface  est ',Rectangle1.surface())
print('volume: ',para.volume())

        
        