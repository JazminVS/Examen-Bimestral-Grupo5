from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("La conjura de los necios")
root.geometry("800x800+450+450")
 
def Call():
    archivo=open("LaConjuradelosNecios.txt","r")
    cont=archivo.read()
    msg=Message(root, text =cont)
    msg.config(bg="lightblue", font=("times",10,"italic"))
    msg.pack()

def Numpalabras ():
    archivo=open("LaConjuradelosNecios.txt","r")
    cont=archivo.read()
    messagebox.showinfo("test","ARCHIVO TXT (#DE PALABRAS): " + str(len(cont.split(" "))))
    

    

numpala = Button(root, text = "LEER NUM.PALABRAS", command = Numpalabras, width=15)
numpala.grid(row=4,column=2)



 
root.mainloop()