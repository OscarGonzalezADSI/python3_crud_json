import funcion
import json


def crud():
    content = Editar()
    contenido = json.dumps(content)
    escribir(contenido)
    end = input()


def Editar():
    content = leer("archivo.json")
    content = json.loads(content)
    registro = content["datos"]
    content["datos"] = Controlador(registro)

    return content


def leer(archivo):
    f = open(archivo, "r")
    content = f.read()
    f.close()

    return content


def Controlador(registro):
    orden = str(input("orden: "))

    if(orden == "insert"):
        rta = insert(registro)
    elif(orden == "update"):
        rta = update(registro)
    elif(orden == "delete"):
        rta = delete(registro)

    return rta


def insert(registro):
    idr = str(len(registro)+1)
    name = str(input("name: "))
    age = str(input("age: "))
    city = str(input("city: "))

    registro[idr] = {
        "1" : name,
        "2" : age,
        "3" : city
    }

    return registro


def update(registro):
    idr = str(input("id: "))
    name = str(input("name: "))
    age = str(input("age: "))
    city = str(input("city: "))

    registro[idr] = {
        "1" : name,
        "2" : age,
        "3" : city
    }

    return registro


def delete(registro):
    idr = str(input("id: "))

    registro[idr] = {
        "1" : "",
        "2" : "",
        "3" : ""
    }

    return registro


def escribir(contenido):
    archivo = "archivo.json"
    f = open(archivo, "w")
    f.write(contenido)
    f.close()




