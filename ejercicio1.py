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
    
creartxt()
print("Calcular n primos")
numero = int(input("Ingrese un numero: "))
for i in range(1, numero):
	primo(i, numero)
	aux=primo1(i,numero)
	grabartxt(aux)


