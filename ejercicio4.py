import goslate
gs=goslate.Goslate()
texto= input("ingresa la palabra:") 
print(gs.translate(texto,'en'))

def creartxt():
	archi=open('EJERCICIO4.txt','w')
	archi.close()
def grabartxt():
	archi=open('EJERCICIO4','a')
	archi.write(gs.translate(texto,'en'))
	archi.close()

creartxt()
grabartxt()