import json
import funcion
import style
from tkinter import *

raiz = Tk()
style.StyleRoot(raiz)

miframe = Frame(raiz)
style.StyleFrame(miframe)
miframe.pack(anchor=NE)

miframe3 = Frame(raiz)
style.StyleFrame(miframe3)
miframe3.pack(anchor=NW)

miframe2 = Frame(raiz)
style.StyleFrame(miframe2)
style.Viewpadding(miframe2, 0)
miframe2.pack()


def RestaurarA(raiz):
    raiz.overrideredirect(False)
    raiz.attributes("-fullscreen", True) #windows raiz.deiconify()
    raiz.geometry("800x600+0+0")
    close.pack_forget()
    maximA.pack_forget()
    restau.pack_forget()
    minim.pack_forget()

    close.pack(side = RIGHT)
    restau.pack(side = RIGHT)
    minim.pack(side = RIGHT)
    raiz.overrideredirect(True)


def RestaurarB(raiz):
    raiz.overrideredirect(False)
    
    raiz.attributes("-fullscreen", False) #windows raiz.deiconify()
    raiz.geometry("800x600+0+0")
    close.pack_forget()
    maximA.pack_forget()
    restau.pack_forget()
    minim.pack_forget()

    close.pack(side = RIGHT)
    maximA.pack(side = RIGHT)
    minim.pack(side = RIGHT)
    raiz.overrideredirect(True)



xxx=StringVar()
yyy=StringVar()


def Ubica(event):
    xxx.set(event.x)
    yyy.set(event.y)

def motion(event):
    xxx.set(str(int(xxx.get())+event.x))
    yyy.set(str(int(yyy.get())+event.y))
    raiz.geometry("800x600+"+str(xxx.get())+"+"+str(yyy.get()))
    print("Mouse position: (%s %s)" % (event.x, event.y))
    print(event.x)



titulo = Label(miframe3, text="Titulo")
minim = Button(miframe, text ="__", command =lambda:RestaurarB(raiz))
maximA = Button(miframe, text ="|_|", command =lambda:RestaurarA(raiz))
restau = Button(miframe, text =" _|", command =lambda:RestaurarB(raiz))
close = Button(miframe, text =" X ", command =lambda:funcion.Salir(raiz))

titulo.config(bg="#000000", fg="#32E282", font='Helvetica 12 bold')
titulo.pack(side = LEFT)
titulo.bind('<B1-Motion>', motion)
titulo.bind('<Button-1>', Ubica)

close.pack(side = RIGHT)
restau.pack(side = RIGHT)
minim.pack(side = RIGHT)

nro = 0
yy = 2
while(yy<10 and nro<24):
    xx = 0
    while(xx<10 and nro<24):
        ViewT = Button(miframe2, text ="Ver tabla"+str(xx)+" "+str(yy), command=funcion.funciones[nro])
        ViewT.config(bg="#32E282", fg="#000000", font='Helvetica 12 bold')
        ViewT.grid(row=yy, column=xx)
        xx=xx+1
        nro=nro+1
    yy=yy+1
    print("------------------------------------------")

raiz.mainloop()
