#Se importa la librería random
from random import *

#Se crea una función para generar números aleatorios
def generarNumeroAleatorio(minimo, maximo):
	try:
		if minimo > maximo:
			aux = minimo
			minimo = maximo
			maximo = aux

		return randint(minimo, maximo)

numero = generarNumeroAleatorio(1, 100)
encontrado = False
intentos = 0

while not encontrado:
	numeroIngresado = int(input("Por favor, ingresa un numero: "))
	if numeroIngresado > numero:
		print("El numero ingresado es mayor que el numero que debes buscar")
		intentos+=1
	elif numeroIngresado < numero:
		print("El numero ingresado es menor que el numero que debes buscar")
		intentos+=1
	elif numeroIngresado == numero:
		encontrado = True
		print("Correcto. Adivinar este numero te ha llevado ", intentos, " intentos.")
