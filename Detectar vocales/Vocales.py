#Inicia el programa 
x = input("Ingresa una vocal, en minuscula o mayuscula: ")

#Función que define si el caracter ingresado es una vocal, devolviendo True
def vocal(x):
	if x == "a" or x == "e" or x == "i"  or x == "o" or x == "u":
		return True
	elif x == "A" or x == "E" or x == "I"  or x == "O" or x == "U":
		return True

	#De lo contrario, devuelve False
	else:
		return False