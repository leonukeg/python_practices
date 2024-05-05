libros = [
    { #0
        "titulo" : "cien años de soledad",
        "autor" : "Gabriel Garcia Marquez",
        "ano" : 1967,
        "genero" : "realismo magico"
    },
    { #1
        "titulo" : "el seño de los anillo",
        "autor" : "J.R.R. Tolkien",
        "ano" : 1954,
        "genero" : "fantasia epica"
    },
    { #2
        "titulo" : "harry potter y la piedra filosofal",
        "autor" : "J.K. rowling",
        "ano" : 1997,
        "genero" : "fantasia juvenil"
    },
    { #3
        "titulo" : "1984",
        "autor" : "Geoerge orwell",
        "ano" : 1949,
        "genero" : "distopia"
    },
    { #4
        "titulo" : "orgullo y prejuicio",
        "autor" : "jane austen",
        "ano" : 1813,
        "genero" : "romance clasico"
    }
    
]

print(type(libros))
print(len(libros))
for i in libros:
    print(i["autor"],)
    
lista1 = [
    [{1,2,3,4}],
    [5,6,7],
    [8,9,0]
]

print(lista1)