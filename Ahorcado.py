# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:36:33 2019

@author: agust
"""
import time
nombre=input ("¿Como te llamás chaboncín?")
print ("Hola"+nombre,"Preparate para la rotura de orto")
print ("")
time.sleep(1)
print ("Agarrate catalina que arrancamos")
time.sleep(0,5)
palabra='cctmexico'
palabra2=''
vidas=3

while vidas > 0:
    fallas=0
    for letra in palabra:
        if letra in palabra2:
            print(letra,end="")
        else:
            print("*",end="")
            fallas+=1
            if fallas==0:
                print 
            
            
            
   