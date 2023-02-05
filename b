#THE GAME
import random


while True:
 print("Bienvenido AL JUEGO")
 print("Elige una opcion para continuar")
 print("A: todo bien wachin")
 print("B: todo mal wacho")
 print("C: Caguemonos a pinias wacho")
 datos = input(": ")

 def B():
     print("Que mal amigo, yo pensaba que estaba todo bien ;O")

 def C():
     print("Plantate wacho")
     x = random.randint(1, 10)
     print("Elegi un numero del 1 al 10")
     pelea = input(": ")
     if pelea == x:
         print("Ganaste, me voy a mi planeta xd")
         
     else:
         print("Moriste men, hasta la proxima")
     

 if datos == "A":
     print("Chau pelotudo, esperaba mas de vos")
     break

 elif datos == "B":
     B()

 elif datos == "C":
     C()