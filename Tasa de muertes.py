# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:42:04 2019

@author: agust
"""
import random
import math
import csv

Machos = random.randint(1,10)
Hembras = random.randint(1,10)
tick = 0

with open('poblacion.csv', 'a', newline='') as csv_file:
    fieldnames = ('tick', 'Machos', 'Hembras')
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writerow({'tick': tick, 'Hembras': Hembras, 'Machos': Machos})
    csv_file.close()
    tick+=1
    print('Tick:', tick)
   
    for x in range(Hembras):
        death=random.randint(1,10000)
        if death <=243:
            Hembras += -1
            
            for x in range(Machos):
                death=random.randint(1,10000)
                if death <=243:
                    Machos += -1
                    
    if crias > 0:
        print (crias, "Estan naciendo los hijitussss!")
        for x in range(crias):
            sexroll = random.randint(1,8)
            if sexroll <= 7:
                Machos += 1
            else:
                Hembras += 1
    
    crias = crias-crias+Egg1
    Egg1 = Egg1-Egg1+Egg2
    Egg2 = Egg2-Egg2+Egg3
    Egg3 = Egg3-Egg3+Egg4
    Egg4 = Egg4-Egg4+Egg5
    Egg5 = Egg5-Egg5+Egg6
    Egg6 = Egg6-Egg6+Egg7
    Egg7 = Egg7-Egg7+Egg8
    Egg8 = Egg8-Egg8+Egg9
    Egg9 = Egg9-Egg9+Egg10
    Egg10 = Egg10-Egg10+Egg11
    Egg11 = Egg11-Egg11+Egg12
    Egg12 = Egg12-Egg12+Egg13
    Egg13 = Egg13-Egg13+Egg14
    Egg14 = Egg14-Egg14+Egg15    
    Egg15 = Egg15-Egg15+Egg16
    Egg16 = Egg16-Egg16+Egg17
    Egg17 = Egg17-Egg17+Egg18
    Egg18 = Egg18-Egg18+Egg19
    Egg19 = Egg19-Egg19+Egg20
    cria20 = cria20-cria20

                
           if Machos >=1 and tick <=100:
                    for x in range(Hembras):
                        crias = random.randint(1,100)
                        if crias <= 50:
                     cria20 +=1
                        elif Hembras >=1:
                         for x in range(Hembras):
                             crias = random.randint(1,100)
                        if crias <=10:
                         cria20 +=1
                         print('Población Total:', Machos+Hembras)
                         print('Hembras:', Hembras)
                         print('Machos', Machos)
                         print()
                          
                         if Hembras + Machos >= 20000:
                              print ('Población Máxima alcanzada')
 