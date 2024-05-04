""" 
escribe una programa que muestre en pantalla todas las fichas del domino
la ficha "en blanco" se puede representar con un 0

0|0 0|1 0|2 0|3 0|4 0|5 0|6
1|1 1|2 1|3 1|4 1|5 1|6
2|2 2|3 2|4 2|5 2|6
3|3 3|4 3|5 3|6
4|4 4|5 4|6
5|5 5|6
6|6

"""
for i in range(0,7): 
    
    for j in range(i,7):
        
        print (f" {i}|{j} ", end = " ") 
        """ 
        la funcion print vacia por defecto me hace un salto de linea, de esta forma luego de imprimir cada par
        me imprime un espacio vacio y asi me imprime todos los pares de j uno al lado de otros
        
        """
    
    print() #de esta forma me imprime un salto de linea juego de imprimir todos los j
    
