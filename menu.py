import goslate
from tkinter import *
from tkinter import messagebox
from math import *

def creartxtEjercicio1():
	archi=open('NumeroPrimo.txt', 'w')
	archi.close()

def grabartxtEjercicio1(num):
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
	creartxtEjercicio1()
	print("Calcular n primos")
	numero = int(input("Ingrese un numero: "))
	for i in range(1, numero):
		primo(i, numero)
		aux=primo1(i,numero)
		grabartxtEjercicio1(aux)

def creartxtEjercicio2():
	archi=open('Multiplo.txt', 'w')
	archi.close()
	
def grabartxtEjercicio2(num):
	archi=open('Multiplo.txt', 'a')
	archi.write(str(num)+"\t")
	archi.close()

def ejercicio2():
	print("2. N multiplos de un numero")
	creartxtEjercicio2()
	print("Multiplos de un numero")
	numeroI = int(input("Ingrese un numero: "))
	numeroM = numeroI
	numeroF = 0
	for i in range(1, 1000):
		print (numeroI)
		grabartxtEjercicio2(numeroI)
		numeroI = numeroI + numeroM
		if numeroI > 1000:
			exit()



def ejercicio3():
	print("3. Contar palabras")
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("La conjura de los necios")
root.geometry("800x800+450+450")

def Numpalabras ():
    archivo=open("LaConjuradelosNecios.txt","r")
    cont1=archivo.read()
    messagebox.showinfo("test","ARCHIVO TXT (#DE PALABRAS): " + str(len(cont1.split(" "))))
    
def Numsaltos ():
    archivo=open("LaConjuradelosNecios.txt","r")
    cont2=archivo.read()
    messagebox.showinfo("test","ARCHIVO TXT (#DE PALABRAS): " + str(len(cont2.split("\n"))))
 
numpala = Button(root, text = "NUM.PALABRAS", command = Numpalabras, width=25)
numpala.grid(row=1,column=1)

numsaltos = Button(root, text = "NUM.SALTOS", command = Numsaltos, width=15)
numsaltos.grid(row=1,column=2)

archivo=open("LaConjuradelosNecios.txt","r")
cont1=archivo.read()
pr1=str(len(cont1.split(" ")))
pr2=str(len(cont1.split("\n")))
p1=open("NUM PALABRAS.txt","w")
p1.write(pr1)
p2=open("NUM SALTOS.txt","w")
p2.write(pr2)

root.mainloop()




def creartxtEjercicio4():
	archi=open('EJERCICIO4.txt','w')
	archi.close()

def grabartxtEjercicio4():
	archi=open('EJERCICIO4','a')
	archi.write(gs.translate(texto,'en'))
	archi.close()

def ejercicio4():
	print("4. Traductor")
	gs=goslate.Goslate()
	texto= input("ingresa la palabra:") 
	print(gs.translate(texto,'en'))
	creartxtEjercicio4()
	grabartxtEjercicio4()




def AreaEsfera ():
	r=float(radio_entry.get()) 
	area=4*pi*(r**2)
	messagebox.showinfo("test","EL AREA ES IGUAL A: %.2f"%area)
	radio_entry.delete(0,20)

def VolumenEsfera ():
	r=float(radio_entry.get()) 
	volumen=4/3*pi*(r**3)
	messagebox.showinfo("test","EL VOLUMEN  ES IGUAL A: %.2f"%volumen)
	radio_entry.delete(0,20)


def ejercicio5():
	print("5. Area y volumen de una esfera")
	app = Tk()
	app.title("CALCULAR AREA Y VOLUMEN DE UNA ESFERA")
	app.geometry("600x100+100+100")

	#PIDIENDO RADIO AL USUARIO
	radio_label = Label(app,text="INGRESE EL RADIO DE LA ESFERA:")
	radio_label.grid(row=1,column=1)
	radio_str = StringVar()
	radio_entry = Entry(app,textvariable=radio_str)
	radio_entry.grid(row=1,column=2)
	#CREANDO BOTONES
	area = Button(app, text = "MOSTRAR AREA", command = AreaEsfera, width=25)
	area.grid(row=4,column=2)

	volumen = Button(app, text = "MOSTRAR VOLUMEN", command = VolumenEsfera, width=25)
	volumen.grid(row=4,column=3)	

	app.mainloop()




def ejercicio6():
	print("6. Tablero raro de ajedrez")
from tkinter import *
tablero = Tk()
canvas = Canvas (tablero, width =700, height =700)
canvas.pack()
canvas.create_line( 45, 80, 90, 10,width =70,fill="black")
canvas.create_line( 115, 80, 160, 10,width =70,fill="black")
canvas.create_line( 45, 220, 90, 150,width =70,fill="black")
canvas.create_line( 115, 290, 160, 220,width =70,fill="black")
canvas.create_line( 45, 360, 90, 290,width =70,fill="black")
canvas.create_line( 115, 430, 160, 360,width =70,fill="black")
canvas.create_line( 45, 500, 90, 430,width =70,fill="black")
canvas.create_line( 115, 570, 160, 500,width =70,fill="black")

canvas.create_line( 185, 80, 230, 10,width =70,fill="black")
canvas.create_line( 255, 150, 300, 80,width =70,fill="black")
canvas.create_line( 185, 220, 230, 150,width =70,fill="black")
canvas.create_line( 255, 290, 300, 220,width =70,fill="black")
canvas.create_line( 185, 360, 230, 290,width =70,fill="black")
canvas.create_line( 255, 430, 300, 360,width =70,fill="black")
canvas.create_line( 185, 500, 230, 430,width =70,fill="black")
canvas.create_line( 255, 570, 300, 500,width =70,fill="black")

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
