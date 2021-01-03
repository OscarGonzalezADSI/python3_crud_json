import json
import funcion
import style
from tkinter import *

raiz = Tk()
raiz.title("ventana de pruebas")
raiz.iconbitmap("our_crud_lite.ico")
raiz.geometry("300x350")
raiz.config(bg="#000000")
raiz.attributes("-fullscreen", True)
raiz.wm_attributes('-alpha',0.8)

miframe = Frame(raiz, width=1200, height=600)
miframe.config(bg="#000000")
miframe.pack()

style.Viewpadding(miframe, 0)

variable = StringVar()
variable.set("0")

def Accion(raiz):
    aaaa = variable.get()
    if(aaaa == "1"):
        Restaurar(raiz)
        variable.set("0")
    else:
        minimizar(raiz)
        variable.set("1")

def Restaurar(raiz):
    raiz.attributes("-fullscreen", True) #windows
    minim.grid(row=0, column=11)
    maxim.grid(row=0, column=12)
    close.grid(row=0, column=13)

def minimizar(raiz):
    raiz.attributes("-fullscreen", False) #windows
    minim.grid_forget()
    maxim.grid_forget()
    close.grid_forget()

minim = Button(miframe, text ="__", command =lambda:Accion(raiz))
maxim = Button(miframe, text ="|_|", command =lambda:Accion(raiz))
close = Button(miframe, text =" X ", command =lambda:funcion.Salir(raiz))


nro = 0
yy = 2
while(yy<10 and nro<24):
    xx = 0
    while(xx<10 and nro<24):
        ViewT = Button(miframe, text ="Ver tabla"+str(xx)+" "+str(yy), command=funcion.funciones[nro])
        ViewT.config(bg="#32E282", fg="#000000", font='Helvetica 12 bold')
        ViewT.grid(row=yy, column=xx)
        xx=xx+1
        nro=nro+1
    yy=yy+1
    print("------------------------------------------")


Restaurar(raiz)

raiz.mainloop()
