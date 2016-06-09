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
