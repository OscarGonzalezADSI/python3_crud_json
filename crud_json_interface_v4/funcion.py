import json
import clase
import Model
import style

from tkinter import *
from tkinter import messagebox

def Expo():

    raiz = Tk()
    raiz.title("ventana de pruebas")
    raiz.iconbitmap("our_crud_lite.ico")
    raiz.geometry("800x600+0-0")
    raiz.config(bg="#000000")
    raiz.wm_attributes('-alpha',0.8)

    miframe = Frame(raiz, width=1200, height=600)
    miframe.config(bg="#000000")
    miframe.pack()

    List(raiz, miframe)

    raiz.mainloop()


def List(raiz, frame):

    style.Viewpadding(frame, 0)

    B = Button(frame, text ="Insert", command=lambda:FormInsert(raiz))
    B.config(bg="#ffffff", fg="#000000", font='Helvetica 12 bold')
    B.grid(row=1, column=0)

    style.ViewTitle(frame, "Registros de Tabla", 1, 1, 3)

    thead(frame, 3)

    contenido = Model.Readjson("archivo.json")
    content = json.loads(contenido)
    ubicacion = 7
    cont = 0

    while(cont<len(content)):

        tbody(raiz, frame, ubicacion, contenido, str(cont+1))
        ubicacion = ubicacion + 1
        cont = cont + 1


def FormInsert(raiz):
    
    raiza = Tk()

    raiza.title(" *** Insert *** ")
    raiza.iconbitmap("our_crud_lite.ico")
    raiza.geometry("400x600+0-0")
    raiza.config(bg="#000000")
    raiza.wm_attributes('-alpha',0.8)
    
    miframe = Frame(raiza)
    miframe.config(bg="#000000")
    miframe.pack()

    style.Viewpadding(miframe, 0)
    style.ViewTitle(miframe, "Insertar Registro", 1, 0, 2)

    miNombre = StringVar()
    miApellido = StringVar()
    miCelular = StringVar()

    miNombre_label = Label(miframe, text="Nombre")
    miNombre_label.config(bg="#000000", fg="#32E282", font='Helvetica 12 bold')
    miNombre_label.grid(row=2, column=0)

    miNombre_input = Entry(miframe, textvariable=miNombre)
    miNombre_input.config(bg="#646161", fg="#ffffff", insertbackground="#ffffff", font='Helvetica 12 bold')
    miNombre_input.grid(row=2, column=1)

    miApellido_label = Label(miframe, text="Apellido")
    miApellido_label.config(bg="#000000", fg="#32E282", font='Helvetica 12 bold')
    miApellido_label.grid(row=3, column=0)

    miApellido_input = Entry(miframe, textvariable=miApellido)
    miApellido_input.config(bg="#646161", fg="#ffffff", insertbackground="#ffffff", font='Helvetica 12 bold')
    miApellido_input.grid(row=3, column=1)

    miCelular_label = Label(miframe, text="Celular")
    miCelular_label.config(bg="#000000", fg="#32E282", font='Helvetica 12 bold')
    miCelular_label.grid(row=4, column=0)

    miCelular_input = Entry(miframe, textvariable=miCelular)
    miCelular_input.config(bg="#646161", fg="#ffffff", insertbackground="#ffffff", font='Helvetica 12 bold')
    miCelular_input.grid(row=4, column=1)

    style.Viewpadding(miframe, 5)


    def accion(raiz, raiza):

        Nombre = miNombre_input.get()
        Apellido = miApellido_input.get()
        Celular = miCelular_input.get()

        Model.Insert(Nombre, Apellido, Celular)

        raiza.destroy()
        raiz.destroy()

        Expo()


    def Cancel(raiz):

        raiz.destroy()


    B = Button(miframe, text ="Cancel", command=lambda:Cancel(raiza))
    B.config(bg="#32E282", fg="#000000", font='Helvetica 12 bold')
    B.grid(row=1, column=2, columnspan=1)

    B = Button(miframe, text ="Save", command=lambda:accion(raiz, raiza))
    B.config(bg="#32E282", fg="#000000", font='Helvetica 12 bold')
    B.grid(row=5, column=2, columnspan=1)

    raiza.mainloop()

def Cancel2(raiz):

    raiz.destroy()

def thead(frame, registro):

    w_label = Label(frame, text="id", bg="#000000", fg="#32E282", font='Helvetica 12 bold')
    w_label.grid(row=registro, column=0)
    

    w_label = Label(frame, text="nombre", bg="#000000", fg="#32E282", font='Helvetica 12 bold')
    w_label.grid(row=registro, column=1)

    w_label = Label(frame, text="apellido", bg="#000000", fg="#32E282", font='Helvetica 12 bold')
    w_label.grid(row=registro, column=2)

    w_label = Label(frame, text="celular", bg="#000000", fg="#32E282", font='Helvetica 12 bold')
    w_label.grid(row=registro, column=3)


def tbody(raiz, frame, registro, con, idr):

    content = json.loads(con)
    campeon = content[idr]

    idr = campeon["idr"]
    nombre = campeon["nombre"]
    apellido = campeon["apellido"]
    celular = campeon["celular"]

    if(nombre == apellido == celular == ""):

        """print("registro "+idr+" eliminado")"""
        print("")

    else:

        w_label = Label(frame, text = idr, bg="#000000", fg="#ffffff", font='Helvetica 12 bold')
        w_label.grid(row=registro, column=0)

        w_label = Label(frame, text = nombre, bg="#000000", fg="#ffffff", font='Helvetica 12 bold')
        w_label.grid(row=registro, column=1)

        w_label = Label(frame, text = apellido, bg="#000000", fg="#ffffff", font='Helvetica 12 bold')
        w_label.grid(row=registro, column=2)

        w_label = Label(frame, text = celular, bg="#000000", fg="#ffffff", font='Helvetica 12 bold')
        w_label.grid(row=registro, column=3)

        w_label = Label(frame, text="", bg="#000000", fg="#ffffff", font='Helvetica 12 bold')
        w_label.grid(row=registro, column=4)

        B = Button(frame, text ="View", command=lambda:View(raiz, con, idr))
        B.config(bg="#32E282", fg="#000000", font='Helvetica 12 bold')
        B.grid(row=registro, column=5)


def View(raiz, con, idr):
    
    content = json.loads(con)
    campeon = content[idr]

    raiza = Tk()

    miNombre = StringVar()
    miApellido = StringVar()
    miCelular = StringVar()

    clase.setNombre(miNombre, campeon["nombre"])
    miNombre = clase.getNombre(miNombre)
    clase.setApellido(miApellido, campeon["apellido"])
    miApellido = clase.getApellido(miApellido)
    clase.setCelular(miCelular, campeon["celular"])
    miCelular = clase.getCelular(miCelular)
    
    raiza.title(" *** View *** ")
    raiza.iconbitmap("our_crud_lite.ico")
    raiza.geometry("400x600+400-0")
    raiza.config(bg="#000000")
    raiza.wm_attributes('-alpha',0.8)

    miframea = Frame(raiza)
    miframea.config(bg="#000000")
    miframea.pack()

    style.Viewpadding(miframea, 0)
    Viewthead(miframea, 0)

    w_label = Label(miframea, text=miNombre)
    w_label.config(bg="#000000", fg="#ffffff", font='Helvetica 12 bold')
    w_label.grid(row=1, column=1)
    w_label = Label(miframea, text=miApellido)
    w_label.config(bg="#000000", fg="#ffffff", font='Helvetica 12 bold')
    w_label.grid(row=2, column=1)
    w_label = Label(miframea, text=miCelular)
    w_label.config(bg="#000000", fg="#ffffff", font='Helvetica 12 bold')
    w_label.grid(row=3, column=1)
    w_label = Label(miframea, text="")
    w_label.config(bg="#000000", fg="#ffffff", font='Helvetica 12 bold')
    w_label.grid(row=4, column=1)

    B = Button(miframea, text ="Delete", command=lambda:FormDelete(raiz, raiza, idr))
    B.config(bg="#32E282", fg="#000000", font='Helvetica 12 bold')
    B.grid(row=5, column=0)
    B = Button(miframea, text ="Update", command=lambda:FormUpdate(raiz, raiza, idr))
    B.config(bg="#32E282", fg="#000000", font='Helvetica 12 bold')
    B.grid(row=5, column=1)

    raiza.mainloop()


def Viewthead(frame, registro):

    w_label = Label(frame, text="nombre")
    w_label.config(bg="#000000", fg="#32E282", font='Helvetica 12 bold')
    w_label.grid(row=1, column=registro)
    w_label = Label(frame, text="apellido")
    w_label.config(bg="#000000", fg="#32E282", font='Helvetica 12 bold')
    w_label.grid(row=2, column=registro)
    w_label = Label(frame, text="celular")
    w_label.config(bg="#000000", fg="#32E282", font='Helvetica 12 bold')
    w_label.grid(row=3, column=registro)


def FormDelete(raiz, raiza, idr):

    raizb = Tk()
    raizb.title(" *** Delete *** ")
    raizb.iconbitmap("our_crud_lite.ico")
    raizb.geometry("400x150+400-0")
    raizb.config(bg="#000000")
    raizb.wm_attributes('-alpha',0.8)

    miframe = Frame(raizb)
    miframe.config(bg="#000000")
    miframe.pack()

    style.Viewpadding(miframe, 0)

    w_label = Label(miframe, text="¿Esta seguro de eliminar este registro?")
    w_label.config(bg="#000000", fg="#ffffff", font='Helvetica 12 bold')
    w_label.grid(row=1, column=0)

    w_label = Label(miframe, text="")
    w_label.config(bg="#000000")
    w_label.grid(row=2, column=0)

    def DelConf(raiz, raiza, raizb, idr):

        Model.Delete(idr)
        WinDelConf(raiz, raiza, raizb)


    B = Button(miframe, text ="Aceptar", command=lambda:DelConf(raiz, raiza, raizb, idr))
    B.config(bg="#32E282", fg="#000000", font='Helvetica 12 bold')
    B.grid(row=3, column=0)
    
    raizb.mainloop()


def WinDelConf(raiz, raiza, raizb):

    raizc = Tk()
    raizc.title(" *** Delete *** ")
    raizc.iconbitmap("our_crud_lite.ico")
    raizc.geometry("400x150+400-0")
    raizc.config(bg="#000000")
    raizc.wm_attributes('-alpha',0.8)

    miframe = Frame(raizc)
    miframe.config(bg="#000000")
    miframe.pack()

    style.Viewpadding(miframe, 0)

    w_label = Label(miframe, text="Registro Eliminado.")
    w_label.config(bg="#000000", fg="#ffffff", font='Helvetica 12 bold')
    w_label.grid(row=1, column=0)

    w_label = Label(miframe, text="")
    w_label.config(bg="#000000")
    w_label.grid(row=2, column=0)


    def accion(raiz, raiza, raizb, raizc):

        raiz.destroy()
        raiza.destroy()
        raizb.destroy()
        raizc.destroy()

        Expo()


    B = Button(miframe, text ="Aceptar", command=lambda:accion(raiz, raiza, raizb, raizc))
    B.config(bg="#32E282", fg="#000000", font='Helvetica 12 bold')
    B.grid(row=3, column=0)
    
    raizc.mainloop()


def FormUpdate(raiz, raiza, idr):
    
    contenido = Model.Readjson("archivo.json")

    content = json.loads(contenido)
    campeon = content[idr]

    nombre = campeon["nombre"]
    apellido = campeon["apellido"]
    celular = campeon["celular"]

    raizb = Tk()
    raizb.title(" *** Update *** ")
    raizb.iconbitmap("our_crud_lite.ico")
    raizb.geometry("400x600+800-0")
    raizb.config(bg="#000000")
    raizb.wm_attributes('-alpha',0.8)

    miframe = Frame(raizb)
    miframe.config(bg="#000000")
    miframe.pack()

    style.Viewpadding(miframe, 0)
    style.ViewTitle(miframe, "Modificar Registro", 1, 0, 2)

    miNombre = StringVar()
    miApellido = StringVar()
    miCelular = StringVar()

    miNombre_label = Label(miframe, text="Nombre")
    miNombre_label.config(bg="#000000", fg="#32E282", font='Helvetica 12 bold')
    miNombre_label.grid(row=2, column=0)

    miNombre_input = Entry(miframe, textvariable=miNombre)
    miNombre_input.config(bg="#646161", fg="#ffffff", insertbackground="#ffffff", font='Helvetica 12 bold')
    miNombre_input.insert(0, nombre)
    miNombre_input.grid(row=2, column=1)

    miApellido_label = Label(miframe, text="Apellido")
    miApellido_label.config(bg="#000000", fg="#32E282", font='Helvetica 12 bold')
    miApellido_label.grid(row=3, column=0)

    miApellido_input = Entry(miframe, textvariable=miApellido)
    miApellido_input.config(bg="#000000", fg="#ffffff", insertbackground="#ffffff", font='Helvetica 12 bold')
    miApellido_input.insert(0, apellido)
    miApellido_input.grid(row=3, column=1)

    miCelular_label = Label(miframe, text="Celular")
    miCelular_label.config(bg="#000000", fg="#32E282", font='Helvetica 12 bold')
    miCelular_label.grid(row=4, column=0)

    miCelular_input = Entry(miframe, textvariable=miCelular)
    miCelular_input.config(bg="#000000", fg="#ffffff", insertbackground="#ffffff", font='Helvetica 12 bold')
    miCelular_input.insert(0, celular)
    miCelular_input.grid(row=4, column=1)

    style.Viewpadding(miframe, 5)


    def accion(raiz, raiza, raizb, idr):
        
        Nombre = miNombre_input.get()
        Apellido = miApellido_input.get()
        Celular = miCelular_input.get()

        Model.Update(idr, Nombre, Apellido, Celular)

        raizb.destroy()
        raiza.destroy()
        raiz.destroy()

        Expo()


    def Cancel(raizb):

        raizb.destroy()


    B = Button(miframe, text ="Cancel", command=lambda:Cancel(raizb))
    B.config(bg="#32E282", fg="#000000", font='Helvetica 12 bold')
    B.grid(row=1, column=2, columnspan=1)
    B = Button(miframe, text ="Save", command=lambda:accion(raiz, raiza, raizb, idr))
    B.config(bg="#32E282", fg="#000000", font='Helvetica 12 bold')
    B.grid(row=5, column=2, columnspan=1)

    raizb.mainloop()


"""

Expo
    List

List
    style.Viewpadding
    FormInsert (Botón de acceso a "FormInsert" del registro.)
    style.ViewTitle
    thead
    Model.Readjson
    json.loads
    while
        tbody
            json.loads
            View (Botón de acceso a la "View" del registro.)

FormInsert
    style.Viewpadding
    style.ViewTitle

thead (Sin novedad.)

View
    json.loads
    style.Viewpadding
    Viewthead
    FormDelete (Botón de acceso a la "FormDelete" del registro.)
    FormUpdate (Botón de acceso a la "FormUpdate" del registro.)

FormDelete
    style.Viewpadding
    Model.Delete
    WinDelConf (Confirmación de eliminación.)

WinDelConf
    style.Viewpadding

FormUpdate
    Model.Readjson
    json.loads
    style.Viewpadding
    style.ViewTitle
    Model.Update
    Expo

"""

def Salir(raiz):
    raiz.destroy()


def ViewTable():
    Expo()


def EsAsi():
    print("Asi es.")


funciones=list(range(25))
funciones[0]= lambda:ViewTable()
funciones[1]= lambda:EsAsi()
funciones[2]= lambda:ViewTable()
funciones[3]= lambda:ViewTable()
funciones[4]= lambda:ViewTable()
funciones[5]= lambda:ViewTable()
funciones[6]= lambda:ViewTable()
funciones[7]= lambda:ViewTable()
funciones[8]= lambda:ViewTable()
funciones[9]= lambda:ViewTable()
funciones[10]= lambda:ViewTable()
funciones[11]= lambda:ViewTable()
funciones[12]= lambda:ViewTable()
funciones[13]= lambda:ViewTable()
funciones[14]= lambda:ViewTable()
funciones[15]= lambda:ViewTable()
funciones[16]= lambda:ViewTable()
funciones[17]= lambda:ViewTable()
funciones[18]= lambda:ViewTable()
funciones[19]= lambda:ViewTable()
funciones[20]= lambda:ViewTable()
funciones[21]= lambda:ViewTable()
funciones[22]= lambda:ViewTable()
funciones[23]= lambda:ViewTable()
funciones[24]= lambda:ViewTable()