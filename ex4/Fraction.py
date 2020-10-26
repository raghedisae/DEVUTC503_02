# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 21:12:48 2019

@author: raghed
"""

class Fraction:
    '''num: numerateur
        denom: denomominateur '''
   
    def __init__(self, n, d):
        self.num = int(n)
        self.denom=int(d)
        if self.denom <0:
            self.denom = abs(self.denom)
            self.num = -1* self.num
        elif self.denom==0:
            raise ZeroDivisionError
    
    def decompose(self,n): 
        res=[]
        i=2 
        while n>1: 
            while n%i==0: 
               res += [i]
               n=n/i 
            i=i+1 
        return res
    
        
    def __str__(self):
        
        if self.denom==1:
            return str(self.num)
        else:
            
            return '%s/%s' %(self.num,self.denom)
    
    def __add__(self,other):
        if self.denom == other.denom:
            self.num = self.num+other.num
            
            #self.num,self.denom
            #self.simplifie()
        else:
            
             self.num*other.denom + other.num*self.denom,self.denom*other.denom
             self.simplifie()

    def __mul__(self,other):
         self.num*other.num,self.denom*other.denom
         self.simplifie()
    
    def simplifie(self):
        nums=self.decompose(self.num)
        denoms=self.decompose(self.denom)
        #print (nums,denoms)
        if(nums==denoms):
            return "1"
        else:
            
            for i in nums:
                
                if i in denoms:
                   self.num=int(self.num/i)
                   
                   self.denom=int(self.denom/i)
                   
                    
                   
         
                
            

if __name__ == '__main__':
    f1 = Fraction(12,6)
    f2 = Fraction(5,6)
    f3=f1+f2
    f4=f1*f2
    #print ()
    print (f3)  
    print (f4)