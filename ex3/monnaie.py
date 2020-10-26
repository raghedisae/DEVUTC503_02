# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:14:24 2019

@author: raghed
"""
class Monnaie(object):
  valeur=0
  devise ='EUR'
    
  def __init__(self, devise):
      self.devise = devise
  
 
  def ajouter(self,val):
      self.valeur += val
      
  
  def retrancher(self,val):
      self.valeur -= val

m1 = Monnaie("EUR")
m2 = Monnaie("EUR")

''' Test 2 devise sont egaux'''
assert m1.devise == m2.devise


m1.ajouter(5)
m2.ajouter(7)
print("Test 1")
print ("valeur de m1:",m1.valeur,m1.devise)
m1.ajouter(m2.valeur)
print ("valeur de m1 apres ajout de m2: ",m1.valeur,m1.devise)


'''deuxieme test'''
m1 = Monnaie("EUR")
m2 = Monnaie("EUR")
''' Test 2 devise sont egaux'''
assert m1.devise == m2.devise

m1.ajouter(5)
m2.ajouter(7)

print("Test 2")
print ("valeur de m1:",m1.valeur,m1.devise)
m1.retrancher(m2.valeur)
print ("valeur de m1 apres retrancher de m2: ",m1.valeur,m1.devise)
