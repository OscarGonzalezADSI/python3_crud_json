import json
import datos
import clase
from tkinter import *
from tkinter import messagebox


def w_group(frame, contenido):

    content = json.loads(contenido)

    txt = content["txt"]
    Lrow = content["Lrow"]
    Lcolumn = content["Lcolumn"]
    Erow = content["Erow"]
    Ecolumn = content["Ecolumn"]

    w_label = Label(frame, text=txt)
    w_label.grid(row=Lrow, column=Lcolumn)
    w_input = Entry(frame)
    w_input.grid(row=Erow, column=Ecolumn)


def experience(campo, Lrow, Lcolumn):

    return json.dumps(datos.wEntry(campo, Lrow, Lcolumn))


def thead(frame, registro):

    w_label = Label(frame, text="id")
    w_label.grid(row=registro, column=0)

    w_label = Label(frame, text="nombre")
    w_label.grid(row=registro, column=1)

    w_label = Label(frame, text="apellido")
    w_label.grid(row=registro, column=2)

    w_label = Label(frame, text="celular")
    w_label.grid(row=registro, column=3)


def FormDelete(raiz, raiza, idr):

    raizb = Tk()

    raizb.title(" *** Delete *** ")
    raizb.iconbitmap("our_crud_lite.ico")
    raizb.geometry("200x100")

    miframeb = Frame(raizb)
    miframeb.pack()

    Viewpadding(miframeb, 0)

    w_label = Label(miframeb, text="Esta seguro de eliminar este registro.")
    w_label.grid(row=1, column=0)
    w_label = Label(miframeb, text="")
    w_label.grid(row=2, column=0)

    B = Button(miframeb, text ="Aceptar", command=lambda:DelConf(raiz, raiza, raizb, idr))
    B.grid(row=3, column=0)
    
    raizb.mainloop()


def WinDelConf(raiz, raiza, raizb):

    raizc = Tk()

    raizc.title(" *** Delete *** ")
    raizc.iconbitmap("our_crud_lite.ico")
    raizc.geometry("200x100")

    miframec = Frame(raizc)
    miframec.pack()

    Viewpadding(miframec, 0)

    w_label = Label(miframec, text="Registro Eliminado.")
    w_label.grid(row=1, column=0)
    w_label = Label(miframec, text="")
    w_label.grid(row=2, column=0)

    B = Button(miframec, text ="Aceptar", command=lambda:closeWinAll(raiz, raiza, raizb, raizc))
    B.grid(row=3, column=0)
    
    raizc.mainloop()


def DelConf(raiz, raiza, raizb, idr):

    Delete(idr)
    
    WinDelConf(raiz, raiza, raizb)


def closeWinAll(raiz, raiza, raizb, raizc):

    raiz.destroy()
    raiza.destroy()
    raizb.destroy()
    raizc.destroy()

    expo()


def FormUpdate(raiz, raiza, idr):
    
    contenido = Readjson("archivo.json")

    content = json.loads(contenido)
    campeon = content[idr]

    nombre = campeon["nombre"]
    apellido = campeon["apellido"]
    celular = campeon["celular"]

    raizb = Tk()

    raizb.title(" *** Update *** ")
    raizb.iconbitmap("our_crud_lite.ico")
    raizb.geometry("300x150")

    miframe = Frame(raizb)
    miframe.pack()

    Viewpadding(miframe, 0)
    ViewTitle(miframe, "Modificar Registro", 1, 1, 1)

    miNombre = StringVar()
    miApellido = StringVar()
    miCelular = StringVar()

    miNombre_label = Label(miframe, text="Nombre")
    miNombre_label.grid(row=2, column=0)
    miNombre_input = Entry(miframe, textvariable=miNombre)
    miNombre_input.insert(0, nombre)
    miNombre_input.grid(row=2, column=1)

    miApellido_label = Label(miframe, text="Apellido")
    miApellido_label.grid(row=3, column=0)
    miApellido_input = Entry(miframe, textvariable=miApellido)
    miApellido_input.insert(0, apellido)
    miApellido_input.grid(row=3, column=1)

    miCelular_label = Label(miframe, text="Celular")
    miCelular_label.grid(row=4, column=0)
    miCelular_input = Entry(miframe, textvariable=miCelular)
    miCelular_input.insert(0, celular)
    miCelular_input.grid(row=4, column=1)

    Viewpadding(miframe, 5)




    def accion(raiz, raiza, raizb, idr):
        

        Nombre = miNombre_input.get()
        Apellido = miApellido_input.get()
        Celular = miCelular_input.get()
        Update(raiz, raiza, raizb, idr, Nombre, Apellido, Celular)




    B = Button(miframe, text ="Cancel", command = View)
    B.grid(row=1, column=2, columnspan=1)
    B = Button(miframe, text ="Save", command =lambda:accion(raiz, raiza, raizb, idr))
    B.grid(row=5, column=2, columnspan=1)

    raizb.mainloop()


def FormInsert(raiz):
    
    raiza = Tk()

    raiza.title(" *** Insert *** ")
    raiza.iconbitmap("our_crud_lite.ico")
    raiza.geometry("300x150")

    miframe = Frame(raiza)
    miframe.pack()

    Viewpadding(miframe, 0)
    ViewTitle(miframe, "Insertar Registro", 1, 1, 1)

    miNombre = StringVar()
    miApellido = StringVar()
    miCelular = StringVar()

    miNombre_label = Label(miframe, text="Nombre")
    miNombre_label.grid(row=2, column=0)
    miNombre_input = Entry(miframe, textvariable=miNombre)
    miNombre_input.grid(row=2, column=1)

    miApellido_label = Label(miframe, text="Apellido")
    miApellido_label.grid(row=3, column=0)
    miApellido_input = Entry(miframe, textvariable=miApellido)
    miApellido_input.grid(row=3, column=1)

    miCelular_label = Label(miframe, text="Celular")
    miCelular_label.grid(row=4, column=0)
    miCelular_input = Entry(miframe, textvariable=miCelular)
    miCelular_input.grid(row=4, column=1)

    Viewpadding(miframe, 5)

    def accion(raiz, raiza):
        Nombre = miNombre_input.get()
        Apellido = miApellido_input.get()
        Celular = miCelular_input.get()
        insert(raiz, raiza, Nombre, Apellido, Celular)

    B = Button(miframe, text ="Cancel", command =lambda:Cancel(raiza))
    B.grid(row=1, column=2, columnspan=1)
    B = Button(miframe, text ="Save", command =lambda:accion(raiz, raiza))
    B.grid(row=5, column=2, columnspan=1)

    raiza.mainloop()


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
    raiza.geometry("200x150")

    miframea = Frame(raiza)
    miframea.pack()

    Viewpadding(miframea, 0)
    Viewthead(miframea, 0)

    w_label = Label(miframea, text=miNombre)
    w_label.grid(row=1, column=1)
    w_label = Label(miframea, text=miApellido)
    w_label.grid(row=2, column=1)
    w_label = Label(miframea, text=miCelular)
    w_label.grid(row=3, column=1)
    w_label = Label(miframea, text="")
    w_label.grid(row=4, column=1)

    B = Button(miframea, text ="Delete", command =lambda:FormDelete(raiz, raiza, idr))
    B.grid(row=5, column=0)
    B = Button(miframea, text ="Update", command =lambda:FormUpdate(raiz, raiza, idr))
    B.grid(row=5, column=1)

    raiza.mainloop()


def tbody(frame, registro, con, idr):

    content = json.loads(con)
    campeon = content[idr]

    w_label = Label(frame, text=campeon["idr"])
    w_label.grid(row=registro, column=0)
    w_label = Label(frame, text=campeon["nombre"])
    w_label.grid(row=registro, column=1)
    w_label = Label(frame, text=campeon["apellido"])
    w_label.grid(row=registro, column=2)
    w_label = Label(frame, text=campeon["celular"])
    w_label.grid(row=registro, column=3)
    w_label = Label(frame, text="")
    w_label.grid(row=registro, column=4)

    B = Button(frame, text ="View", command=lambda:View(con, idr))
    B.grid(row=registro, column=5)


def tbody2(raiz, frame, registro, con, idr):

    content = json.loads(con)
    campeon = content[idr]

    idr = campeon["idr"]
    nombre = campeon["nombre"]
    apellido = campeon["apellido"]
    celular = campeon["celular"]

    if(nombre == apellido == celular == ""):

        print("registro "+idr+" eliminado")

    else:
        w_label = Label(frame, text = idr)
        w_label.grid(row=registro, column=0)
        w_label = Label(frame, text = nombre)
        w_label.grid(row=registro, column=1)
        w_label = Label(frame, text = apellido)
        w_label.grid(row=registro, column=2)
        w_label = Label(frame, text = celular)
        w_label.grid(row=registro, column=3)
        w_label = Label(frame, text="")
        w_label.grid(row=registro, column=4)

        B = Button(frame, text ="View", command=lambda:View(raiz, con, idr))
        B.grid(row=registro, column=5)


def Viewpadding(frame, registro):

    w_label = Label(frame, text="")
    w_label.grid(row=registro, column=0)


def ViewTitle(frame, titleTable, registro, col, colspan):

    w_label = Label(frame, text=titleTable)
    w_label.grid(row=registro, column=col, columnspan=colspan)


def Viewthead(frame, registro):

    w_label = Label(frame, text="nombre")
    w_label.grid(row=1, column=registro)
    w_label = Label(frame, text="apellido")
    w_label.grid(row=2, column=registro)
    w_label = Label(frame, text="celular")
    w_label.grid(row=3, column=registro)


def Viewtbody(frame, registro):

    w_label = Label(frame, text="oscar")
    w_label.grid(row=1, column=registro)
    w_label = Label(frame, text="gonzalez")
    w_label.grid(row=2, column=registro)
    w_label = Label(frame, text="3228858439")
    w_label.grid(row=3, column=registro)

    B = Button(frame, text ="View", command = View)
    B.grid(row=registro, column=4)


def Readjson(archivo):

    f = open(archivo, "r")
    content = f.read()
    f.close()
    return content


def List(raiz, frame):

    contenido = Readjson("archivo.json")
    content = json.loads(contenido)
    ubicacion = 7
    cont = 0

    while(cont<len(content)):
        tbody2(raiz, frame, ubicacion, contenido, str(cont+1))
        ubicacion = ubicacion + 1
        cont = cont + 1


def escribir(contenido):

    archivo = "archivo.json"
    f = open(archivo, "w")
    f.write(contenido)
    f.close()


def Cancel(raiz):

    raiz.destroy()


def insert(raiz, raiza, Nombre, Apellido, Celular):

    contenido = Readjson("archivo.json")
    content = json.loads(contenido)
    ubicacion = 7
    cont = 0

    idr = str(int(len(content)+1))
    campeon = idr

    content[idr] = {
        "idr" : idr,
        "nombre" : Nombre,
        "apellido" : Apellido,
        "celular" : Celular
    }

    contenido = json.dumps(content)
    escribir(contenido)
    raiz.destroy()
    raiza.destroy()
    expo()


def Delete(idr):

    contenido = Readjson("archivo.json")
    content = json.loads(contenido)
    ubicacion = 7
    cont = 0

    content[idr] = {
        "idr" : idr,
        "nombre" : "",
        "apellido" : "",
        "celular" : ""
    }

    contenido = json.dumps(content)
    escribir(contenido)
    

def Update(raiz, raiza, raizb, idr, Nombre, Apellido, Celular):

    contenido = Readjson("archivo.json")
    content = json.loads(contenido)
    ubicacion = 7
    cont = 0

    content[idr] = {
        "idr" : idr,
        "nombre" : Nombre,
        "apellido" : Apellido,
        "celular" : Celular
    }

    contenido = json.dumps(content)
    escribir(contenido)
    raizb.destroy()
    raiza.destroy()
    raiz.destroy()
    expo()

def expo():

    raiz = Tk()

    raiz.title("ventana de pruebas")
    raiz.iconbitmap("our_crud_lite.ico")
    raiz.geometry("300x350")

    miframe = Frame(raiz, width=1200, height=600)
    miframe.pack()

    Viewpadding(miframe, 0)

    B = Button(miframe, text ="Insert", command =lambda:FormInsert(raiz))
    B.grid(row=1, column=0)

    ViewTitle(miframe, "Registros de Tabla", 1, 1, 3)

    thead(miframe, 3)

    List(raiz, miframe)

    raiz.mainloop()

