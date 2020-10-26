# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:27:12 2019

@author: raghed
"""

class Date(object):
 
    
    def __init__(self,day,month,year):
        '''check if days and months are correct'''
        if day <1 or day >31:
            raise AssertionError("jour doit etre entre 1 et 31",day)
        if month <1 or month >12:
            raise AssertionError("moit doit etre entre 1 et 12",month)
        if year <0:
            raise AssertionError("anne doit etre entre >0",year)
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
         return(str(self.day)+"/"+str(self.month)+"/"+str(self.year))

d=Date(1,12,2020)
#print (d.day,"/",d.month,"/",d.year)
print (d)