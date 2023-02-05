# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 20:55:02 2019

@author: agust
"""

import random
import csv


m = random.randint(1,10)
h = random.randint(1,10)
tick = 0
Egg0 = 0
Egg1 = 0
Egg2 = 0
Egg3 = 0
Egg4 = 0
Egg5 = 0
Egg6 = 0
Egg7 = 0
Egg8 = 0
Egg9 = 0
Egg10 = 0
Egg11 = 0
Egg12 = 0
Egg13 = 0
Egg14 = 0
Egg15 = 0
Egg16 = 0
Egg17 = 0
Egg18 = 0
Egg19 = 0
Egg20 = 0

with open('Poblacion.csv', 'a', newline='') as csv_file:
        fieldnames = ['tick', 'Hembras', 'Machos']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        csv_file.close()

while True:
    with open('Poblacion.csv', 'a', newline='') as csv_file:
        fieldnames = ['tick', 'Hembras', 'Machos']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'tick': tick, 'Hembras': h, 'Machos': m})
        csv_file.close()
    tick += 1
    print("Tick:", tick)
    for x in range(h):
        death = random.randint(1,10000)
        if death <= 243:
            h += -1
            

    for x in range(m):
        death = random.randint(1,10000)
        if death <= 243:
            m += -1
            
    
    if Egg0 > 0:
        print (Egg0, "ESTAN SALIENDO HIJITUSSSS!")
        for x in range(Egg0):
            sexroll = random.randint(1,8)
            if sexroll <= 7:
                m += 1
            else:
                h += 1
    
    Egg0 = Egg0-Egg0+Egg1
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
    Egg20 = Egg20-Egg20



    if m >=1 and tick <=100:
        for x in range(h):
            egg = random.randint(1,100)
            if egg <= 50:
                Egg20 += 1
                
    elif h >=1:
        
        for x in range(h):
            egg = random.randint(1,100)
            if egg <=10:
                Egg20 += 1

              
    
    print("Población Total:", h+m)
    print("Hembras:", h)
    print("Machos:", m)
    print("")


    if h+m >= 20000:
        print("Población Máxima Alcanzada")

        break
    elif h == 0 and Egg0 == 0 and Egg1 == 0 and Egg2 == 0 and Egg3 == 0 and Egg4 == 0 and Egg5 == 0 and Egg6 == 0 and Egg7 == 0 and Egg8 == 0 and Egg9 == 0 and Egg10 == 0 and Egg11 == 0 and Egg12 == 0 and Egg13 == 0 and Egg14 == 0 and Egg15 == 0 and Egg16 == 0 and Egg17 == 0 and Egg18 == 0 and Egg19 == 0 and Egg20 == 0:
        
        print("Hasta la proxima")
        break