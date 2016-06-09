def creartxt():
	archi=open('NumeroPrimo.txt', 'w')
	archi.close()
def grabartxt(num):
	archi=open('NumeroPrimo.txt', 'a')
	archi.write(str(num))
	archi.close()

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
