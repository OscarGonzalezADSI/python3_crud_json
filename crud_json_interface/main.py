import json
import funcion
import style
from tkinter import *

raiz = Tk()

raiz.title("ventana de pruebas")
raiz.iconbitmap("our_crud_lite.ico")
raiz.geometry("300x350")

miframe = Frame(raiz, width=1200, height=600)
miframe.pack()

style.Viewpadding(miframe, 0)

B = Button(miframe, text ="Ver tabla", command =lambda:funcion.Expo())
B.grid(row=1, column=0)

raiz.mainloop()
