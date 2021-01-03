import json

def Insert(Nombre, Apellido, Celular):

    contenido = Readjson("archivo.json")
    content = json.loads(contenido)

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


def Update(idr, Nombre, Apellido, Celular):

    contenido = Readjson("archivo.json")
    content = json.loads(contenido)

    content[idr] = {
        "idr" : idr,
        "nombre" : Nombre,
        "apellido" : Apellido,
        "celular" : Celular
    }

    contenido = json.dumps(content)
    escribir(contenido)


def Delete(idr):

    contenido = Readjson("archivo.json")
    content = json.loads(contenido)

    content[idr] = {
        "idr" : idr,
        "nombre" : "",
        "apellido" : "",
        "celular" : ""
    }

    contenido = json.dumps(content)
    escribir(contenido)


def Readjson(archivo):

    f = open(archivo, "r")
    content = f.read()
    f.close()
    return content


def escribir(contenido):

    archivo = "archivo.json"
    f = open(archivo, "w")
    f.write(contenido)
    f.close()


