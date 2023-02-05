#Se declaran las variables
texto1 = input("Por favor, ingresa un texto: ")
texto2 = input("Ahora, ingresa otro texto:")

#Se devuelve el resultado uniendo las dos cadenas de texto y se intercambian los 2 primeros carácteres de cada cadena
print(cadena2[:2] + cadena1[2:] + " " + cadena1[:2] + cadena2[2:])  