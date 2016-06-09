n, cont = 4, 2
num = int(input("Ingrese un numero: "))
if(num > 2):
 cad = "2 - 3"
 while cont < num:
  i=2
  while i<=num:
   if(i==n):
    cad= cad+" - "+str(i)
    cont=cont+1
   else:
    if(n % i ==0):
     i=n
   i=i+1
  n=n+1
 print(cad)
else:
 if(num>0):
  if(num==1):
   print("es primo 2")
  else:
   print("es primo 2, 3")
 else:
  print("ingrese un numero positivo")

//FUNCION PARA DETMINAR SI UN NUMERO ES UN PRIMO 
def primo(num):
  a=0
  for i range(1, n+1):
    if(num%i==0):
      a=a+1
    if(a!=2):
      print("No es primo")
    else:
      print("es primo")


