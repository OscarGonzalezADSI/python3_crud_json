import json
import funcion
import datos
from tkinter import *

raiz = Tk()

raiz.title("ventana de pruebas")
raiz.iconbitmap("our_crud_lite.ico")
raiz.geometry("300x350")

miframe = Frame(raiz, width=1200, height=600)
miframe.pack()

funcion.Viewpadding(miframe, 0)

B = Button(miframe, text ="Ver tabla", command =lambda:funcion.expo())
B.grid(row=1, column=0)

raiz.mainloop()
