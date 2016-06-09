print("Multiplos de un numero")
numeroI = int(input("Ingrese un numero: "))
numeroM = numeroI
numeroF = 0
for i in range(1, 1000):
    print (numeroI)
    numeroI = numeroI + numeroM
    if numeroI > 1000:
        exit()
