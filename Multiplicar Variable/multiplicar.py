
def generar_n_caracteres(cantidad, caracter):
	print cantidad * caracter

print "Hola, por favor introduce un caracter a multiplicar: "
caracteres = input("Introduce el caracter: ")
print "Ahora, introduce la cantidad de veces que se multiplicara"
cantidades = input("Introduce la cantidad: ")

generar_n_caracteres(cantidades, caracteres)