
def creartxt():
	archi=open('NumeroPrimo.txt', 'w')
	archi.close()
def grabartxt(num):
	archi=open('NumeroPrimo.txt', 'a')
	archi.write(str(num)+"\t")
	archi.close()

def primo(num, n):
	a = 0
	for i in range(1, n +1):
		if(num % i == 0):
		a = a + 1
	if(a == 2):
	print("es primo: " +str(num))
	return num

def primo1(num, n):
	a = 0
	for i in range(1, n +1):
	if(num % i == 0):
		a = a + 1
	if(a == 2):
		return num

def ejercicio1():
	print("1. N numeros primos")
	creartxt()
	print("Calcular n primos")
	numero = int(input("Ingrese un numero: "))
	for i in range(1, numero):
		primo(i, numero)
		aux=primo1(i,numero)
		grabartxt(aux)

def creartxt():
	archi=open('Multiplo.txt', 'w')
	archi.close()
	
def grabartxt(num):
	archi=open('Multiplo.txt', 'a')
	archi.write(str(num)+"\t")
	archi.close()

def ejercicio2():
	print("2. N multiplos de un numero")
	creartxt()
	print("Multiplos de un numero")
	numeroI = int(input("Ingrese un numero: "))
	numeroM = numeroI
	numeroF = 0
	for i in range(1, 1000):
		print (numeroI)
		grabartxt(numeroI)
		numeroI = numeroI + numeroM
		if numeroI > 1000:
			exit()

def ejercicio3():
	print("3. Contar palabras")

def ejercicio4():
	print("4. Traductor")

def ejercicio5():
	print("5. Area y volumen de una esfera")

def ejercicio6():
	print("6. Tablero raro de ajedrez")


print("ESCUELA POLITECNICA NACIONAL")
print("ESCUELA DE FORMACION DE TECNOLOGOS")
print("\nPROGRAMACION AVANZADA")
print("1. N numeros primos")
print("2. N multiplos de un numero")
print("3. Contar palabras")
print("4. Traductor")
print("5. Area y volumen de una esfera")
print("6. Tablero raro de ajedrez")
print("7. Salir")
opcion = int(input("Elija una opcion: "))
if opcion == 1:
	ejercicio1()
if opcion == 2:
	ejercicio2()
if opcion == 3:
	ejercicio3()
if opcion == 4:
	ejercicio4()
if opcion == 5:
	ejercicio5()
if opcion == 6:
	ejercicio6()
if opcion == 7:
	exit()