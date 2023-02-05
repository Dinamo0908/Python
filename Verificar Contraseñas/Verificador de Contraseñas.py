#Verificar contrasenas
import user
import user2
import time

def validar():
 correct = False
 while correct == False:
  print ("Por favor, ingrese su nombre de usuario.")
  ch2 = input (": ")
  if user.nickname(ch2) == True:
   print ("El nombre de usuario " + ch2 + " a sido verficado con exito. Cargando siguiente fase...")
   correct = True
   time.sleep(3)
 while correct == True:
   print ("Por favor, ingrese su password.")
   ch3 = input (": ")
   if user2.contra(ch3) == True:
     print ("La contrasenia " + ch3 + " a sido verficada con exito.") 
     print ("Recuerda: tu usuario es " + ch2 + " y tu contrasenia es " + ch3)
     correct = False
     time.sleep(3)
     print ("Adios!")

def init():
 ch1 = input(": ")
 if ch1 == "si":
  validar()
 elif ch1 == "no":
  print ("Entonces, nos vemos luego!")
 else: 
  print ("No te he entendido. Quieres intentarlo de vuelta?")
  time.sleep(3)
  init()

print ("Hola! Interesado en verificar que tan fuerte es tu password? Si es asi, escribe 'si' ahora.")
init()
