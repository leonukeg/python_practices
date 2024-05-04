""" 
hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
-recorrer la lista y mostrarla
-hacer una funcion que recorra listas de numero y devuelva un string
-ordenar y mostrarla 
-mostrar su longitud
-buscar algun elemento (que el usuario pida por teclado)
"""

number = [34,56,24,74,90,32,45,99]
print(f"The list is: {number} \n")
print(f"The data type is: {type(number)} \n")
long = len(number)
print(f"The length of the list is: {long} \n")
number = sorted(number) 
print(f"The ordered list is: {number} \n")

def recorrer():
    
    for i in range(len(number)):
        x = number[i]
        print(f"element {i} is {x}")
        
recorrer()

element = int(input("que elemento desea de la lista"))
if element < long:
    print(f"element {element} of the list is: {number[element]}")
else:
    print("The list is not that long bro")
