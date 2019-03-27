# Autor: Martha Margarita Dorantes Cordero
# calcular divisones y encontrar el mayor

def dividir(dividendo, divisor) :
	cociente = 0
	residuo = dividendo
	while residuo >= divisor :
		cociente += 1
		residuo = residuo - divisor
	print(' %d / %d = %d, sobra %d'%(dividendo, divisor, cociente, residuo))


def encontrarMayor() :
	numero = 0
	mayor = -1
	while numero != -1:
		numero = int(input(" Teclea un nÃºmero [-1 para salir]: "))
		if numero >= mayor :
			mayor = numero
	if mayor == -1 :
		print(" No hay valor mayor")
	else :
		print(' El mayor es: %d'%(mayor))


def main() :
	print("\n Mision 07")
	print(" 1. Calcular divisiones")
	print(" 2. Encontrar el mayor")
	print(" 3. Salir")
	opcion = int(input(" Teclea tu opciÃ³n: "))
	if opcion == 1 :
		print("\n Calculando divisiones")
		dividendo = int(input(" Dividendo: "))
		divisor = int(input(" Divisor: "))
		dividir(dividendo, divisor)
		input(" Presione enter para continuar...")
		main()
	elif opcion == 2 :
		print("\n Teclea una serie de nÃºmeros para encontrar el mayor.")
		encontrarMayor()
		input(" Presione enter para continuar...")
		main()
	elif opcion == 3 :
		print("\n Gracias por usar este programa, regresa pronto.")
		exit(0)
	else :
		print(" ERROR, teclea 1, 2 o 3")
		main()


main()