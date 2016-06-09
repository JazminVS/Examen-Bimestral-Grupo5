from  textblob import TextBlob
import sys 
from tkinter import *
def hacer_click ():
	try:
	 _palabra= str(entrada_texto.get())
	 _palabra=(_palabra)
	 etiqueta.config(text=_palabra)
	except ValueError:
	 etiqueta.config(text="INGRESE UN NUMERO: ")
	 text = _palabra
	 blob1 = TextBlob(text)
	 blob1.tags
	 blob1.noun_phrases
	 etiqueta (blob1.translate (to = "en")) ##"en" en esta parte se pone el idionma al que se quiere traducir
	 for sentence in blob1.sentences:
		 etiqueta(sentence.sentiment.polarity)
		 

app=Tk()
app.title("MI SEGUNDA APP GRAFICA")

#CUADRO DE TEXTO
vp=Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)

etiqueta=Label(vp, text="traducción")
etiqueta.grid(column=2, row=2, sticky=(W,E))

boton=Button(vp, text="TRADUCIR", command=hacer_click)
boton.grid(column=1, row=1)

palabra= ""
entrada_texto=Entry(vp, width=20, textvariable=palabra)
entrada_texto.grid(column=2, row=1)

app.mainloop()