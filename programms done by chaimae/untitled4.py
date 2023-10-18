# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 20:45:59 2023

@author: pc
"""

class Personne:
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age
    def afficher1(self):
        print(f"Nom: {self.nom}")
        print("Prenom : ", self.prenom)
        print(" age  : ", self.age )

class Adherant(Personne):
    def __init__(self,nom,prenom,age,numadherant):
        self.numadherant=numadherant
        super().__init__(nom,prenom,age)
    def afficher(self):
        print(" numero de l'adherant '  : ", self.numadherant )
        super().afficher1()

class Auteur(Personne):
    def __init__(self,nom,prenom,age,numauteur):
        self.numauteur=numauteur
        super().__init__(nom,prenom,age)
    def afficher(self):
        print(" numero de l'auteur '  : ", self.numauteur )
        super().afficher1()


class Livre:
    def __init__(self,isbn,titre,auteurs):
        self.isbn=isbn
        self.titre=titre
        self.auteurs=auteurs
    def afficher2(self):
        print(" isbn  : ", self.isbn )
        print(" titre  : ", self.titre )
        print('les auteurs : ')
        for auteur in self.auteurs:
            print(f"- {auteur}")
            
class bibliotheque:
    def main():
        adherant=Adherant("chaimae", "bouassab", 20, 4323)
        livre=Livre(7697,"bonheur",["hhhhh","ouuou"])
        adherant.afficher()
        livre.afficher2()

bibliotheque.main()

        
    
    
        
        
        