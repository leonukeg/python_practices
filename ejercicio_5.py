""" 
crear una lista con el contenido de esta table 
ACCION AVENTURA DEPORTES 
GTA ASSINS FIFA 21 
COD CRASH PRO 21
PUGB PRINCE OF PERSIA MOTO GP 21 

MOSTRAR ESTA INFORMACION ORDENADA

"""

tabla = [
    {
        "categoria" : "ACCION",
        "JUEGOS" : ["GTA", "COD", "PUGB"]
    },
    {
        "categoria" : "AVENTURA",
        "JUEGOS" : ["assins", "crash", "PDP"]
    },
    {
        "categoria" : "DEPORTE",
        "JUEGOS" : ["FIFA", "PRO", "MOTO GP"]
    },
]

for i in tabla:
    print(f"-----------{i["categoria"]}-------------")
    for j in i["JUEGOS"]:
        print(j)