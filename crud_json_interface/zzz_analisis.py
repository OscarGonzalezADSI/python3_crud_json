import json

def leer(archivo):
    f = open(archivo, "r")
    content = f.read()
    f.close()

    return content


def Editar():
    content = leer("archivo.json")
    content = json.loads(content)

    return content


def crud():
    content = Editar()
    contenido = json.dumps(content)
    escribir(contenido)
    end = input()



def unif(archivo):
    f = open(archivo, "r")
    content = f.read()
    f.close()
    
    content = json.loads(content)

    contenido = json.dumps(content)
    escribir(contenido)
    end = input()


def unif2(archivo):
    f = open(archivo, "r")
    content = f.read()
    f.close()
    
    content = json.loads(content)

    print(len(content))
    end = input()

unif2("archivo.json")


















