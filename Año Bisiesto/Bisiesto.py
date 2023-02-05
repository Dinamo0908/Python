#Se crea una función para comprobar años bisiestos
def bisiesto():
	a = input("Escriba un anio para comprobar si es bisiesto")
	if a % 4 == 0 and (not(a % 100 == 0)):
		print("El anio ", a, " es un anio bisiesto")
	else:
		print("El anio", a, " no es bisiesto")
