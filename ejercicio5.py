#CALCULANDO AREA Y VOLUMEN DE UNA ESFERA 

from tkinter import *
from tkinter import messagebox
from math import*

app = Tk()
app.title("CALCULAR AREA Y VOLUMEN DE UNA ESFERA")
app.geometry("600x100+100+100")

#PIDIENDO RADIO AL USUARIO
radio_label = Label(app,text="INGRESE EL RADIO DE LA ESFERA:")
radio_label.grid(row=1,column=1)
radio_str = StringVar()
radio_entry = Entry(app,textvariable=radio_str)
radio_entry.grid(row=1,column=2)

#FUNCIONES A CALCULAR
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

#CREANDO BOTONES
area = Button(app, text = "MOSTRAR AREA", command = AreaEsfera, width=25)
area.grid(row=4,column=2)

volumen = Button(app, text = "MOSTRAR VOLUMEN", command = VolumenEsfera, width=25)
volumen.grid(row=4,column=3)	

app.mainloop()
