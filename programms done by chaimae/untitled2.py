# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 11:17:07 2023

@author: pc
"""

class CompteBancaire:
    def __init__(self,NumeroCompte,nom,solde):
        self.num=NumeroCompte
        self.nom=nom
        self.solde=solde
    def versement(self,money):
        self.solde= self.solde+money
    def retrait(self,money):
        if(self.solde> money):
            self.solde= self.solde-money
        else:
            print(' impossible de retirer')
    def afficher(self):
        print(f"Compte numéro : {self.num}")
        print("Nom : ", self.nom)
        print(" Solde  : ", self.solde )



c1=CompteBancaire(435,' chaimae', 24)
c1.versement(2)
c1.retrait(58796)
c1.afficher()

        