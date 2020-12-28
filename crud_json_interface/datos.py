import json


def wEntry(campo, Lrow, Lcolumn):
    Lcolumn2 = Lcolumn+1
    value = {
        "txt" : campo,
        "Lrow" : Lrow,
        "Lcolumn" : Lcolumn,
        "Erow" : Lrow,
        "Ecolumn" : Lcolumn2
    }
    return value

registro = {}

registro["1"] = {
    "idr" : "1",
    "nombre" : "julia",
    "apellido" : "perra",
    "celular" : "3228858439"
}

registro["2"] = {
    "idr" : "2",
    "nombre" : "oscar",
    "apellido" : "gonzalez",
    "celular" : "3134563202"
}

registro["3"] = {
    "idr" : "3",
    "nombre" : "ricardo",
    "apellido" : "sandoval",
    "celular" : "55555555"
}

"""
def escribir(contenido):
    archivo = "archivo.json"
    f = open(archivo, "w")
    f.write(contenido)
    f.close()

contenido = json.dumps(registro)
escribir(contenido)
"""

