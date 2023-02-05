#Calculadora


while True:
  print("Opciones:")
  print("Escribe \"sumar\" para sumar dos numeros")
  print("Escribe \"restar\" para restar dos numeros")
  print("Escribe \"multiplicar\" para multiplicar dos numeros")
  print("Escribe \"dividir\" para dividir dos numeros")
  print("Escribe \"salir\" para salir del programa")
  user_input = input(": ")

  if user_input == "salir":
  	break

  elif user_input == "sumar":
   num1 = float(input("Elige un numero: "))
   num2 = float(input("Elige otro numero: "))
   result = str(num1 + num2)
   print("La respuesta es " + result)
   print("Adios!")
   break

  elif user_input == "restar":
   num1 = float(input("Elige un numero: "))
   num2 = float(input("Elige otro numero: "))
   result = str(num1 - num2)
   print("La respuesta es " + result)
   print("Adios!")
   break
   

  elif user_input == "multiplicar":
   num1 = float(input("Elige un numero: "))
   num2 = float(input("Elige otro numero: "))
   result = str(num1 * num2)
   print("La respuesta es " + result)
   print("Adios!")
   break
   

  elif user_input == "dividir":
   num1 = float(input("Elige un numero: "))
   num2 = float(input("Elige otro numero: "))
   result = str(num1 / num2)
   print("La respuesta es " + result)
   print("Adios!")
   break